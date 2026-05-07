import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:

    """
    Changes the data type of the 'grade' column to integer.

    Rule:
    - Convert all values in 'grade' column from float to int
    """
    students['grade'] = students['grade'].astype(int)
    return students
