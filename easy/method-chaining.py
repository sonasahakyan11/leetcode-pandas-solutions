import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:

    """
    Returns the names of animals with weight greater than 100.

    Rules:
    - Keep only animals with weight > 100
    - Sort results by weight in descending order
    - Return only the 'name' column
    """
    animals = animals[animals['weight']>100].sort_values('weight', ascending=False)
    return animals[['name']]
