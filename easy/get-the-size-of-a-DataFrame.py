import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    """
    Returns the number of rows and columns in a DataFrame.

    Output format:
    [rows, columns]
    """
    return list(players.shape)
