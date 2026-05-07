import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:

    """
    Concatenates two DataFrames vertically.

    Rule:
    - Rows from df2 are appended below df1
    """
    return pd.concat([df1, df2])
