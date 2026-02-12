import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    df = person
    df.sort_values(by = "id", ascending = True, inplace = True)
    df.drop_duplicates(subset = ['email'], keep = 'first', inplace = True)
    