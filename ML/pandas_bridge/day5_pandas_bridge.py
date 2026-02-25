from typing import List
import pandas as pd
class PandasBridge:
    def rank_salaries(self,df:pd.DataFrame)->pd.DataFrame:
        df["rank"]=df.groupby("department")["salary"].rank(
            method="dense",
            ascending=False
        )
        return df


if __name__=="__main__":
    data={
        'employee_name':['Alice','Bob','Charlie','David','Eve','Frank'],
        'department':['IT','IT','IT','HR','HR','HR'],
        'salary':[90000,80000,120000,70000,80000,90000]
    }
    df=pd.DataFrame(data)
    solver=PandasBridge()
    result_df=solver.rank_salaries(df)
    print(result_df)