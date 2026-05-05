import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby("sell_date", as_index=False).agg(
      
        # number of unique products per day
        num_sold=("product", "nunique"),

        # unique products concatenated into a string
        products=("product", lambda x: ",".join(sorted(x.unique())))
    )
