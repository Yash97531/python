import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity
    df.drop(columns={'device_id', 'games_played'}, inplace = True)
    a = df.groupby('player_id')['event_date'].min().reset_index()
    a.rename(columns = {'event_date' : 'first_login'}, inplace = True)
    return a