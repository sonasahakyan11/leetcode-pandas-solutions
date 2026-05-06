import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    """
    Returns users with valid LeetCode email addresses.

    Rules:
    - Starts with a letter
    - Contains letters, digits, underscore, dot, or hyphen
    - Ends with @leetcode.com
    """
    return users[
        users['mail'].str.match(
            r'^[A-Za-z][\w_\.-]*@leetcode\.com$', 
            na=False
        )
    ]
