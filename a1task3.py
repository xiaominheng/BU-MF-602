#
# a1task3.py - Assignment 1, Task 3
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Functions for time value of money calculations
#

# function 0
def fv_lump_sum(r, n, pv):
    """ future value of a lump sump pv invested at the periodic rate r for n periods
        input r: interest rate
        input n: periods
        input pv: present value
    """
    return pv * pow(1 + r, n)

# function 1
def pv_lump_sum(r, n, fv):
    """ present value of a lump sum fv to be received in the future
        input r: interest rate
        input n: periods
        input fv: future value
    """
    return fv / pow(1 + r, n)

# function 2
def fv_annuity(r, n, pmt):
    """future value of an annuity of pmt to be received each period for n periods,
       invested at the periodic rate r.
       input r: interest rate
       input n: periods
       input pmt: annuity per period
    """
    ratio = (pow(1 + r, n) - 1) / r
    return pmt * ratio

# function 3
def pv_annuity(r, n, pmt):
    """
    present value of an annuity of pmt to be received each period for n periods, discounted at the rate r
    input r: interest rate
    input n: periods
    input pmt: annuity per period
    """
    ratio = (1 - pow(1 + r, -n)) / r
    return pmt * ratio

# function 4
def annuity_payment(r, n, pv):
    """
    annuity payment for a present value of pv to be repaid at a periodic interest rate of r for n periods
    input r: interest rate
    input n: periods
    input pv: annuity's present value
    """
    return r * pv / (1 - pow(1 + r, -n))


""" 
Testing Part
if __name__ == '__main__':

    # Tests for function 0
    print("$100 at 5% rate for 2 years", fv_lump_sum(0.05, 2, 100))
    print("$400 at 8% APR for 20 years (with monthly compounding)", fv_lump_sum(0.08 / 12, 20 * 12, 400))

    # Tests for function 1
    print("$1000 to be received in 5 years at 6% per year", pv_lump_sum(0.06, 5, 1000))
    print("$500 received in 5 years, 6% APR, semi-ann. compounding", pv_lump_sum(0.06/2, 5*2, 500))

    # Tests for function 2
    print("invest $100 per year for 5 years at 4% interest", fv_annuity(0.04, 5, 100))
    print("invest $100 per month for 10 years at 9% APR", fv_annuity(0.09/12, 10*12, 100))

    # Tests for function 3
    print("pv of 30 payments of $250 per year, 5% interest", pv_annuity(0.05, 30, 250))
    print("pv of 60 payments of $471.75 per month, 0.9% APR", pv_annuity(0.009/12,60, 471.75))

    # Tests for function 4
    print("annuity payment for pv of $1,000 for 10 year at 5%", annuity_payment(0.05, 10, 1000))
    print("annuity payment for pv of $27,667 for 60 months at 0.9% APR", annuity_payment(0.009/12, 60, 27667.44))
"""