import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses
    a = df.groupby('class', as_index=False)['student'].count()
    b = a[a['student'] >= 5]
    c = b.drop(columns = {'student'})
    return c