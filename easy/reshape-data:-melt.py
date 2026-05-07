import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:

   """
    Reshapes the report DataFrame from wide format to long format.

    Rules:
    - Keep 'product' column unchanged
    - Convert quarter columns into rows
    - Store quarter names in 'quarter' column
    - Store sales values in 'sales' column
    """
    return pd.melt(
        report,
        id_vars='product',
        value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
        var_name='quarter',
        value_name='sales'
    )
