import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge employee and department tables on department id
    df = pd.merge(
        employee, 
        department, 
        left_on = 'departmentId', 
        right_on = 'id', 
        how = 'inner', 
        suffixes = ('_left', '_right'))
  
    # Rank salaries within each department (highest salary gets rank 1)
    df['dense_rank'] = df.groupby('name_right')['salary'].rank(
        method='dense', 
        ascending=False)

    # Keep only top 3 salaries per department, select and rename final output columns
    return df[df['dense_rank'] <= 3][['name_right', 'name_left', 'salary']].rename(
        columns={
        'name_right': 'Department',
        'name_left': 'Employee',
        'salary': 'Salary'
    })
