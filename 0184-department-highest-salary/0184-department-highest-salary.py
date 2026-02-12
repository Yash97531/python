import pandas as pd
import numpy as np
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df1 = employee
    df2 = department
    df = pd.merge(df1, df2 ,left_on = 'departmentId', right_on = 'id', how = 'left')
    df.rename(columns = {'name_x' : "Employee", 'name_y' : 'Department', 'salary' : 'Salary'}, inplace = True)
    df.sort_values(by = 'Salary', ascending = False, inplace = True)
    df['max_salary'] = df.groupby("Department")['Salary'].transform(max)
    df.drop(columns = {'id_x', 'departmentId', 'id_y'}, inplace = True)
    df['bool'] = df['Salary'] != df['max_salary']
    a = df[df['bool'] == False]
    a.drop(columns = {'bool', 'max_salary'}, inplace = True)
    return a[['Department', 'Employee', 'Salary']]