import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """
    Replace NaN values in 'quantity' with 0
    """
    products['quantity'] = products['quantity'].fillna(0)
    return products
