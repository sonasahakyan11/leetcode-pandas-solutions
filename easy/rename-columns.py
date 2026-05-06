import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    Renames columns in the students DataFrame for better readability.

    Column mapping:
    - id → student_id
    - first → first_name
    - last → last_name
    - age → age_in_years
    """
    # Rename multiple columns using a mapping dictionary
    # inplace=True modifies the original DataFrame directly
    students.rename(
        columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
        },
        inplace=True
    )

    return students
