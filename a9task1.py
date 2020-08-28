#
# a9task1.py - Assignment 9, Task 1
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Backtesting a Trading Strategy
#
import numpy as np
import pandas as pd
# Puzzle1:
def create_bollinger_bands(df, window = 21, no_of_std = 1, column_name = ''):
    """

    :param df:
    :param window:
    :param no_of_std:
    :param column_name:
    :return:
    """
    df2 = pd.DataFrame()
    if column_name == '':
        if df.columns[0] == 'Date':
            column_name = df.columns[1]
        else:
            column_name = df.columns[0]
    df2['Observation'] = df[column_name]
    df2['RollingMean'] = df2['Observation'].rolling(window).mean()
    df2['UpperBound'] = df2['RollingMean'] + no_of_std * df2['Observation'].rolling(window).std()
    df2['LowerBound'] = df2['RollingMean'] - no_of_std * df2['Observation'].rolling(window).std()
    return df2[['Observation', 'RollingMean', 'UpperBound', 'LowerBound']]

# Puzzle2:
def create_long_short_position(df):
    """

    :param df:
    :return:
    """
    df2 = df.copy(deep = True)
    def position_judge(df):
        if df['Observation'] > df['UpperBound']:
            return 1
        elif df['Observation'] < df['LowerBound']:
            return -1
        else:
            return None

    df2['Position'] = df2.apply(position_judge, axis=1)
    df2['Position'].fillna(method='ffill', inplace=True)
    return pd.DataFrame(df2['Position'])

# Puzzle3:
def calculate_long_short_returns(df, position, column_name = ''):
    """

    :param df:
    :param position:
    :param column_name:
    :return:
    """
    if column_name == '':
        if df.columns[0] == 'Date':
            column_name = df.columns[1]
        else:
            column_name = df.columns[0]
    df2 = df.copy(deep=True)
    df2['Position'] = position
    df2['Market Return'] = (df[column_name] - df[column_name].shift(1))/df[column_name].shift(1)
    df2['Strategy Return'] = df2['Position'] * df2['Market Return']
    df2['Abnormal Return'] = df2['Strategy Return'] - df2['Market Return']
    return df2[['Market Return', 'Strategy Return', 'Abnormal Return']]


# Puzzle4:
def plot_cumulative_returns(df):
    """

    :param df:
    :return:
    """
    for i in df.columns:
        df[i] = df[i].cumsum()
    df.plot()


