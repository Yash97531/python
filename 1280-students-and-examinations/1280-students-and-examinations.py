import pandas as pd
import numpy as np
def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df1 = students
    df2 = subjects
    df3 = examinations
    a = df1.merge(df2, how="cross")
    exam_counts = (df3.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams'))
    result = a.merge(exam_counts, on=['student_id', 'subject_name'],how='left').fillna({'attended_exams' : 0})
    result['attended_exams'] = result['attended_exams'].astype(int)
    result = result.sort_values(['student_id', 'subject_name'])
    return result