import pandas as pd
import numpy as np 

def calculate_volatility(file_name):
    """
    This function takes the name or loaction of datset and create dataframe.
    Using data frameit calculate the Daily Volatility and Annualized Volatility.
    It return the result of calculation in dict or json format.
    """
    # Reading dataset using pandas 
    df = pd.read_csv(f'{file_name}') #Creating dataframe 

    # Removing whitesapces if present
    df.columns = [col.strip() for col in df.columns]

    # Converting date to pandas datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

    # Setting date column as index
    df.set_index('Date', inplace=True)

    # Daily returns
    df['DailyReturns'] = df['Close'].pct_change()

    # Daily Volatility
    daily_volatility = np.std(df['DailyReturns'])

    # Annualized Volatility
    trading_days = 252 # Taken avg trading days in year
    annualize_volatility = daily_volatility * np.sqrt(trading_days)

    res = {
        "daily_volatility": daily_volatility,
        "annualize_volatility": annualize_volatility
    }

    return res

