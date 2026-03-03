import pandas as pd
import numpy as np


class FeatureEngineering:

    def apply_log_transform(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        Applies log1p transformation to reduce right skew.
        """
        if column in df.columns:
            df[f"{column}_log"] = np.log1p(df[column])
        return df

    def target_encode(self, df: pd.DataFrame, categorical_col: str, target_col: str) -> pd.DataFrame:
        """
        Applies basic target encoding (without cross-validation).
        WARNING: This naive implementation may cause data leakage.
        """
        mean_target = df.groupby(categorical_col)[target_col].mean()
        df[f"{categorical_col}_encoded"] = df[categorical_col].map(mean_target)
        return df


if __name__ == "__main__":
    data = {
        "zip_code": ["500032", "500081", "500032", "500084"],
        "price": [9000000, 7500000, 11000000, 6500000]
    }

    df = pd.DataFrame(data)

    fe = FeatureEngineering()

    df = fe.apply_log_transform(df, "price")
    df = fe.target_encode(df, "zip_code", "price")

    print(df)