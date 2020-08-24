#
# a6task3.py - Assignment 6, Task 3
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Matrix Application: Bond Pricing
#

from a4task1 import cashflow_times, bond_cashflows, discount_factors
from a6task1 import *
from a6task2 import *

# Puzzle1: re-implement the bond_price function
def bond_price(fv, c, n, m, r):
    """
    :param fv: future value
    :param c: coupon rate
    :param n: maturity
    :param m: payment frequency
    :param r: risk-free rate
    :return: bond price
    """
    bond_cf = bond_cashflows(fv, c, n, m)
    discount_rate = discount_factors(r, n, m)
    return dot_product([discount_rate], transpose([bond_cf]))

# Puzzle2: Find the implied prices of zero-coupon bonds
def bootstrap(cashflows, prices):
    """
    :param cashflows: A matrix of cashflows
    :param prices: A matrix of prices
    :return: Implied prices of zero-coupon bonds
    """
    return dot_product(inverse_matrix(cashflows), prices)
