import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets
    df['length'] = df['content'].str.len()
    new = df[df['length'] > 15]
    a = new.drop(columns = {'content', 'length'})
    return a