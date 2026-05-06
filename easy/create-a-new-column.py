import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:

    """
    Adds a new column 'bonus' to the DataFrame.

    Rule:
    - bonus is calculated as 2 times the employee's salary
    """

    employees['bonus'] = employees['salary']*2
    return employees
