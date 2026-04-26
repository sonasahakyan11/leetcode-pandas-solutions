import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
  
    """
    Fix capitalization of names and sort by user_id
    """
    users['name'] = users['name'].str.capitalize()
    users = users.sort_values(by = 'user_id')
    return users
