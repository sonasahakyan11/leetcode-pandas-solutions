import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the first 3 rows of the DataFrame.
    """
    return employees[0:3]
