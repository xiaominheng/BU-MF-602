#
# a8task1.py - Assignment 8, Task 1
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Simulating Stock Returns
#
import numpy as np
import math
import matplotlib.pyplot as plt
class MCStockSimulator:
    # Puzzle1: define __init__ and __repr__
    def __init__(self, s, t, r, sigma, nper_per_year):
        """
        :param s: The current stock price in dollars
        :param t: The option maturity time in years
        :param r: The annualized rate of return on this stock
        :param sigma: The annualized standard deviation of returns
        :param nper_per_year: The number of discrete time periods per year
        """
        self.s = s
        self.t = t
        self.r = r
        self.sigma = sigma
        self.nper_per_year = nper_per_year

    def __repr__(self):
        """

        :return:
        """
        return "StockSimulator(s=$%.2f, t = %.2f(years), r = %.2f, sigma = %.2f, nper_per_year = %d" %\
               (self.s, self.t, self.r, self.sigma, self.nper_per_year)

    def generate_simulated_stock_returns(self):
        """

        :return:
        """
        dt = 1 / self.nper_per_year
        z_array = np.random.normal(0, 1, int(self.nper_per_year * self.t))
        return (self.r - self.sigma**2/2) * dt + z_array*self.sigma*dt**0.5

    def generate_simulated_stock_values(self):
        """

        :return: Return an array of stock price
        """
        stock_price = [self.s]
        returns = self.generate_simulated_stock_returns()
        for i in range(int(self.t * self.nper_per_year)):
            stock_price.append(stock_price[i]*math.e**returns[i])
        return np.array(stock_price)

    def plot_simulated_stock_values(self, num_trials=1):
        """

        :param num_trials:
        :return:
        """
        x = np.arange(0, self.t+1/self.nper_per_year, 1/self.nper_per_year)
        for i in range(num_trials):
            plt.plot(x, self.generate_simulated_stock_values())
        plt.xlim(0, self.t)
        plt.xticks(np.arange(0, self.t+0.25, 0.25))
        plt.xlabel("years")
        plt.ylabel("$ value")
        plt.title("%d simulated trials" % num_trials)
        plt.show()
