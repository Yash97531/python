import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, left_on = "id", right_on = "customerId" , how = 'left')
    a = df[df['customerId'].isna()]
    b = a.drop(columns = {'id_x', 'id_y', 'customerId'})
    b.rename(columns = {'name' : 'Customers'}, inplace = True)
    return b