import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:

    """
    Reshapes the weather DataFrame using a pivot table.

    Rules:
    - Rows are indexed by 'month'
    - Unique values from 'city' become columns
    - 'temperature' values fill the table
    """
    return weather.pivot(index='month', columns='city', values='temperature')
