import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df = students
    df.dropna(subset = ['name'], inplace = True)
    return df