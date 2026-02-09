import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals
    new = df[df['weight']>100]
    new = new.sort_values(by="weight", ascending=False)

    a = new.drop(columns = {'species', 'age', 'weight'})
    return a