import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Removes rows where the 'name' column has missing values.

    Rule:
    - Keeps only rows where 'name' is not NaN
    """
    return students.dropna(subset='name')
