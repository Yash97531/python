import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df.sort_values(by = 'emp_id', ascending = True, inplace = True)
    df['total_time'] = (df['out_time'] - df['in_time'])
    df.drop(columns = {'in_time', 'out_time'}, inplace = True)
    a = df.groupby(['emp_id','event_day'])['total_time'].sum().reset_index()
    a.rename(columns = {'event_day' : 'day'}, inplace = True)
    return a[['day', 'emp_id', 'total_time']]