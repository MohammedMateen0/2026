import pandas as pd
import numpy as np
import sqlite3
import logging
import re
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)
class HyderabadDataPipeline:
    def __init__(self,db_path:str):
        self.db_path=db_path
    def extract(self,file_path:str)->pd.DataFrame:
        logging.info(f"Extracting data....{file_path}")
        try:
            df=pd.read_csv(file_path)
            logging.info("Extraction completed.")
            return df
        except Exception as e:
            logging.error(f"Extraction failed: {e}")
            raise
    def clean_currency_columns(self, df: pd.DataFrame, column_name: str) -> pd.DataFrame:

        logging.info(f"Cleaning currency column: {column_name}")

        def convert(value):
            if pd.isna(value):
                return np.nan

            value = str(value).strip().replace(",", "")

            try:
                if "Cr" in value:
                    number = float(re.findall(r"\d+\.?\d*", value)[0])
                    return number * 1e7
                elif "L" in value:
                    number = float(re.findall(r"\d+\.?\d*", value)[0])
                    return number * 1e5
                else:
                    return float(re.findall(r"\d+\.?\d*", value)[0])
            except:
                return np.nan

        if column_name in df.columns:
            df[column_name] = df[column_name].apply(convert)
        else:
            logging.warning(f"Column {column_name} not found")

        return df
        
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:

        logging.info("Handling missing values...")

        if "location" in df.columns:

            numeric_cols = df.select_dtypes(include=[np.number]).columns

            for col in numeric_cols:
                df[col] = df.groupby("location")[col].transform(
                    lambda x: x.fillna(x.median())
                )

        categorical_cols = df.select_dtypes(include=["object"]).columns

        for col in categorical_cols:
            df[col] = df[col].fillna("Unknown")

        logging.info("Missing values handled.")

        return df

    def load_to_sqlite(self,df:pd.DataFrame,table_name:str):
        logging.info("Connecting to SqLite database...")
        try:
            conn=sqlite3.connect(self.db_path)
            df.to_sql(
                table_name,
                conn,
                if_exists='replace',
                index=False
            )
            logging.info("Data successfully loaded to SQLite.")
        except Exception as e:
            logging.error(f"Database load failed:{e}")
            raise
        finally:
            if conn:
                conn.close()
                logging.info("Database connection  closed.")
