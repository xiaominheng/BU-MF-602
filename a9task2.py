#
# a9task1.py - Assignment 9, Task 1
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Calculating Drawdown
#
from a8task1 import *
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt

# Puzzle1:
def compute_drawdown(prices):
    """

    :param prices:
    :return:
    """
    df = pd.DataFrame(index=prices.index)
    prices = np.array(prices)
    df['price'] = prices
    df['prev_max'] = np.array([max(max(prices[:i]), prices[i]) if i != 0 else prices[0] for i in range(len(prices))])
    df['dd_dollars'] = df.apply(lambda x: x['prev_max'] - x['price'], axis=1)
    df['dd_pct'] = df.apply(lambda x: x['dd_dollars'] / x['prev_max'], axis=1)
    return df

# Puzzle2:
def plot_drawdown(df):
    """

    :param df:
    :return:
    """
    df[['price', 'prev_max']].plot()
    plt.title("Price and Previous Maximum")
    plt.show()

    df['dd_pct'].plot()
    plt.title("Drawdown Percentage")
    plt.show()

# Puzzle3:
def run_mc_drawdown_trials(init_price, years, r, sigma, trial_size, num_trials):
    """

    :param init_price:
    :param years:
    :param r:
    :param sigma:
    :param trial_size:
    :param num_trials:
    :return:
    """
    dd_pct = []
    for i in range(num_trials):
        simu = MCStockSimulator(init_price, years, r, sigma, trial_size)
        prices = pd.Series(simu.generate_simulated_stock_values())
        dd_pct.append(max(compute_drawdown(prices)['dd_pct']))
    return pd.Series(dd_pct)
