import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the name and age of the student with student_id = 101.

    Steps:
    - Filter rows where student_id equals 101
    - Select only the 'name' and 'age' columns
    """
    return students[students['student_id']==101][['name', 'age']]
