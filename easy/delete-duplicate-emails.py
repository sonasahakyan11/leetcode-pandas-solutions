import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """
    Remove duplicate emails in-place, keeping the row with the smallest id.
    
    Returns:
    None: The DataFrame is modified in-place.
    """
    person.sort_values("id", inplace=True)
    person.drop_duplicates(subset="email", keep="first", inplace=True)
    person.reset_index(drop=True, inplace=True)
