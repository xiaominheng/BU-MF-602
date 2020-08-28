#
# a8task2.py - Assignment 8, Task 2
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Pricing Path-Dependent Options
#
from a8task1 import *

class MCStockOption(MCStockSimulator):
    # Puzzle1
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        """

        :param s:
        :param x:
        :param t:
        :param r:
        :param sigma:
        :param nper_per_year:
        :param num_trials:
        """
        super().__init__(s, t, r, sigma, nper_per_year)
        self.x = x
        self.num_trials = num_trials

    def __repr__(self):
        """

        :return:
        """
        return "MCStockOption, s=%.2f, x=%.2f, t=%.2f, r=%.2f, sigma=%.2f, nper_per_year=%d, num_trials=%d" %\
               (self.s, self.x, self.t, self.r, self.sigma, self.nper_per_year, self.nper_per_year)

    # Puzzle2
    def value(self):
        """

        :return:
        """
        print("Base class MCStockOption has no concrete implementation of .value().")
        return 0

    def stderr(self):
        """

        :return:
        """
        # dir() return all the attributes in the class
        # stdev will be added in the inherited classes
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)

        return 0

class MCEuroCallOption(MCStockOption):
    # Puzzle3:
    def __repr__(self):
        """

        :return:
        """
        return "MCEuroCallOption, s = %.2f, x = %.2f, t = %.2f, r = %.2f,\
         sigma = %.2f, nper_per_year = %d, num_trials = %d" % (self.s, self.x, self.t, self.r, self.sigma,
                                                               self.nper_per_year, self.num_trials)
    def value(self):
        """

        :return:
        """
        price_list = []
        for _ in range(self.num_trials):
            price_list.append(self.generate_simulated_stock_values()[-1])
        call_price_list = []
        for i in range(len(price_list)):
            call_price_list.append(max(price_list[i]-self.x, 0) / math.e**(self.r * self.t))
        self.stdev = np.array(call_price_list).std()
        return np.array(call_price_list).mean()

class MCEuroPutOption(MCStockOption):
    """

    """
    def __repr__(self):
        """

        :return:
        """
        return "MCEuroPutOption, s = %.2f, x = %.2f, t = %.2f, r = %.2f,\
                 sigma = %.2f, nper_per_year = %d, num_trials = %d" % (self.s, self.x, self.t, self.r, self.sigma,
                                                                       self.nper_per_year, self.num_trials)

    def value(self):
        """

        :return:
        """
        price_list = []
        for _ in range(self.num_trials):
            price_list.append(self.generate_simulated_stock_values()[-1])
        put_price_list = []
        for i in range(len(price_list)):
            put_price_list.append(max(self.x-price_list[i], 0) / math.e**(self.r * self.t))
        self.stdev = np.array(put_price_list).std()
        return np.array(put_price_list).mean()

class MCAsianCallOption(MCStockOption):
    def __repr__(self):
        """

        :return:
        """
        return "MCAsianCallOption, s = %.2f, x = %.2f, t = %.2f, r = %.2f,\
                 sigma = %.2f, nper_per_year = %d, num_trials = %d" % (self.s, self.x, self.t, self.r, self.sigma,
                                                                       self.nper_per_year, self.num_trials)
    def value(self):
        """

        :return:
        """
        price_list, asian_call = [], []
        for _ in range(self.num_trials):
            price_list.append(self.generate_simulated_stock_values())
        for i in range(len(price_list)):
            asian_call.append(max(np.mean(price_list[i]) - self.x, 0)/math.e**(self.r * self.t))
        self.stdev = np.std(asian_call)
        return np.mean(asian_call)


class MCAsianPutOption(MCStockOption):
    def __repr__(self):
        """

        :return:
        """
        return "MCAsianPutOption, s = %.2f, x = %.2f, t = %.2f, r = %.2f,\
                 sigma = %.2f, nper_per_year = %d, num_trials = %d" % (self.s, self.x, self.t, self.r, self.sigma,
                                                                       self.nper_per_year, self.num_trials)
    def value(self):
        """

        :return:
        """
        price_list, asian_call = [], []
        for _ in range(self.num_trials):
            price_list.append(self.generate_simulated_stock_values())
        for i in range(len(price_list)):
            asian_call.append(max(self.x - np.mean(price_list[i]), 0)/math.e**(self.r * self.t))
        self.stdev = np.std(asian_call)
        return np.mean(asian_call)

class MCLookbackCallOption(MCStockOption):
    def __repr__(self):
        """

        :return:
        """
        return "MCLookbackCallOption, s = %.2f, x = %.2f, t = %.2f, r = %.2f,\
                 sigma = %.2f, nper_per_year = %d, num_trials = %d" % (self.s, self.x, self.t, self.r, self.sigma,
                                                                       self.nper_per_year, self.num_trials)
    def value(self):
        """

        :return:
        """
        price_list, lookback_call = [], []
        for _ in range(self.num_trials):
            price_list.append(self.generate_simulated_stock_values())
        for i in range(len(price_list)):
            lookback_call.append(max(max(price_list[i]) - self.x, 0) / math.e**(self.r * self.t))
        self.stdev = np.std(lookback_call)
        return np.mean(lookback_call)

class MCLookbackPutOption(MCStockOption):
    def __repr__(self):
        """

        :return:
        """
        return "MCLookbackPutOption, s = %.2f, x = %.2f, t = %.2f, r = %.2f,\
                 sigma = %.2f, nper_per_year = %d, num_trials = %d" % (self.s, self.x, self.t, self.r, self.sigma,
                                                                       self.nper_per_year, self.num_trials)
    def value(self):
        """

        :return:
        """
        price_list, lookback_put = [], []
        for _ in range(self.num_trials):
            price_list.append(self.generate_simulated_stock_values())
        for i in range(len(price_list)):
            lookback_put.append(max(self.x - min(price_list[i]), 0) / math.e**(self.r * self.t))
        self.stdev = np.std(lookback_put)
        return np.mean(lookback_put)


