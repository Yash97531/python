import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world
    new = df[(df['population'] >= 25000000 )|( df['area']>= 3000000)]
    a = new.drop(columns = {'continent', 'gdp'})
    return a