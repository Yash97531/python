import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = sales_person
    df2 = company 
    df3 = orders
    df1.drop(columns={'salary', 'commission_rate', 'hire_date'}, inplace = True)
    df2.drop(columns={'city'}, inplace = True)
    df3.drop(columns={'amount', 'order_date', 'order_id'}, inplace = True)
    a = df1.merge(df3, on = 'sales_id', how = 'left').fillna(0)
    b = a.merge(df2, on = 'com_id', how = 'left').fillna(0)
    d = b[b['name_y'] == "RED"]
    c = df1.merge(d, on = 'sales_id', how = 'left').fillna(99999)
    names = c[c['name_x'] == 99999]
    return names[['name']]