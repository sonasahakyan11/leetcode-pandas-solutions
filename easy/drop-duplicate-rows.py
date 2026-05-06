import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate customer records based on email.

    """
   return customers.drop_duplicates(subset='email')
