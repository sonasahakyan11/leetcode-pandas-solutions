import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    # Merge products and orders on 'product_id' (inner join keeps only matching rows)
    merged = products.merge(orders, on='product_id', how='inner')

    # Filter orders in February 2020
    # Then group by product_name and calculate total units sold per product
    result = (
        merged.loc[
            (merged['order_date']>='2020-02-01') & 
            (merged['order_date']<'2020-03-01')
        ].groupby(
            'product_name', 
            as_index=False
        ).agg(
            unit=('unit', 'sum')
        )
    )
  
    # Keep only products with total units >= 100
    return result[result['unit']>=100]
