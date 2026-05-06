import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:

    """
    Creates a pandas DataFrame from a 2D list of student data.

    Each inner list represents a row in the format:
    [student_id, age]

    Returns: pd.DataFrame: DataFrame with columns 'student_id' and 'age'
    """
    return pd.DataFrame(student_data, columns=['student_id', 'age'])
