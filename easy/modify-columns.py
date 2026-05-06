import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Modifies the 'salary' column by doubling each value.

    Rule:
    - salary = salary * 2 for every employee
    """
    employees['salary'] = employees['salary']*2
    return employees
