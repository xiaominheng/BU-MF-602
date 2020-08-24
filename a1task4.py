#
# a1task4.py - Assignment 1, Task 4
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: The Life-Cycle Model of Saving and Consumption
#

from a1task3 import *


def life_cycle_model():
    """ No input parameter
        return all stat items.
    """
    print("Welcome to the Life-Cycle Sustainable Spending Calculator.\n")
    
    # Puzzle1: Collect the input of rish-free rate, current age, expected retire age and income per year.
    r = float(input("Enter the current inflation-indexed risk-free rate of return: "))
    age = int(input("Enter your age now: "))
    retire_age = int(input("Enter your expected retirement age: "))
    income = int(input("Enter your current annual income: "))
    print("\nYou have {} remaining working years with an income of ${} per year.".format(retire_age - age, income))

    # Puzzle2: Calculate the human capital
    human_capital = pv_annuity(r, retire_age - age, income)
    print("The present value of your human capital is about ${}".format(int(human_capital)))

    # Puzzle3: Prompt the user for the amount of current assets
    # ........ If no asset, input 0, if debt, input a negative number
    asset = int(input("Enter the value of your financial assets: "))
    net_worth = human_capital + asset
    print("Your economic net worth is: ${}\n".format(int(net_worth)))

    # Puzzle4: Calculate the sustainable standard of living
    consumption = annuity_payment(r, 100 - age, net_worth)
    print("Your sustainable standard of living is about ${} per year.".format(int(consumption)))

    # Puzzle5: Calculate the amount of annual savings required
    savings = income - consumption
    print("To achieve this standard of living to age 100, you must save ${} per year.".format(int(savings)))


if __name__ == '__main__':
    life_cycle_model()
