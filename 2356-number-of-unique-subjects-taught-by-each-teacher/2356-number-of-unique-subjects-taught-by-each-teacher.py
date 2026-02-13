import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher
    df.drop(columns = {'dept_id'}, inplace = True)
    df.drop_duplicates(subset={'teacher_id', 'subject_id'}, inplace= True)
    a = df.groupby('teacher_id', as_index=False)['subject_id'].count()
    a.rename(columns = {'subject_id' : 'cnt'}, inplace=True)
    return a