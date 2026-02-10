import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = users
    df['name'] = df['name'].str.lower()
    df['name'] = df['name'].str.capitalize()
    df.sort_values(by = 'user_id', ascending = True, inplace = True)
    return df