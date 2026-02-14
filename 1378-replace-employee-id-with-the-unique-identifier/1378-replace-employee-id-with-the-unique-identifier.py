import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df1 = employees
    df2 = employee_uni
    a = pd.merge(df1, df2, on = "id", how = 'left')
    a.drop(columns = {'id'}, inplace = True)
    return a[['unique_id', 'name']]