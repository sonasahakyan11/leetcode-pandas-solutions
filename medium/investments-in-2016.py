import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # Find rows where tiv_2015 is NOT unique (appears more than once)
    df_dup_tiv_2015 = insurance[insurance.duplicated(subset=['tiv_2015'], keep=False)]
    
    # Find rows with unique (lat, lon) combinations
    df_unique_loc = insurance.drop_duplicates(subset=['lat', 'lon'], keep=False)

    # Keep only rows whose pid exists in both conditions, sum tiv_2016
    result =  df_dup_tiv_2015[df_dup_tiv_2015['pid'].isin(df_unique_loc['pid'])]['tiv_2016'].sum()

    # Return result as a DataFrame with required formatting
    return pd.DataFrame({
        'tiv_2016': [round(result, 2)]
    })
