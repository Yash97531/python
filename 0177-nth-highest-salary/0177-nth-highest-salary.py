import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee
    a = df.drop_duplicates(subset = ['salary'], keep = 'first')
    if (len(a) < N or N<= 0):
        import numpy as np
        return pd.DataFrame({f"getNthHighestSalary({N})": [np.nan]})
    else:
        a.sort_values(by = "salary", ascending = False, inplace = True)
        d = a['salary'].iloc[N-1] 
        dct = {f"getNthHighestSalary({N})" : [d]}
        return pd.DataFrame(dct)