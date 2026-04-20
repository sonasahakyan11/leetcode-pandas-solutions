import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    """
    Combine Person and Address tables using LEFT JOIN on 'personId'
    - Keeps all records from Person table
    - Missing addresses will appear as NaN
    """
    joined_df = pd.merge(person, address, on='personId', how='left')
    return joined_df[['firstName', 'lastName', 'city', 'state']]
