#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Starter code for assignment 12.

@author: azs
"""
import sqlite3 as db
import pandas as pd


# These queries will help you discover the database schema (structure).

example_0a = '''SELECT name FROM sqlite_master''' # select all tables in database
example_0b = '''pragma table_info(clients)''' # get the info from "clients" table
example_0c = '''pragma table_info(trades)''' # get the info from "trades" table
example_0d = '''pragma table_info(price_history)''' # get the info from "price_history" table


# This is an example query that you can use to get started:
## QUERY 00 SHOW ALL CLIENTS IN DATABASE
sql_00 = '''
SELECT * 
FROM price_history
WHERE price_history.date == '2020-03-31'
'''
## QUERY 01 SHOWS ALL PRICE HISTORY RECORDS ON 2020-03-31 ORDERED BY SECURITY
sql_01 = '''
SELECT *
FROM price_history
WHERE date == '2020-03-31'
ORDER BY security
'''

## QUERY 02 SHOWS ALL RECORDS FOR CLIENT ANGELA MERKEL ORDERED BY TRADE DATE
sql_02 = '''
SELECT *
FROM trades
WHERE client_id == 4
ORDER BY trade_date
'''

## QUERY 03
sql_03 = '''
SELECT *
FROM trades
WHERE '2018-12-31' < trade_date AND trade_date < '2020-01-01'
ORDER BY trade_date
'''

## QUERY 04
sql_04 = '''
SELECT security AS name, COUNT(security) AS count
FROM trades
GROUP BY security
ORDER BY security
'''

## QUERY 05
sql_05 = '''
SELECT first_name, last_name, COUNT(trades.client_id) AS number
FROM clients
INNER JOIN trades
ON clients.client_id == trades.client_id
GROUP BY trades.client_id
ORDER BY number DESC
'''

## QUERY 06
sql_06 = '''
SELECT first_name, last_name, quantity, trades.security, trade_date
FROM trades
INNER JOIN clients
ON trades.client_id == clients.client_id
WHERE security == 'CSCO'
ORDER BY trade_date
'''

## QUERY 07
sql_07 = '''
SELECT trade_date, first_name, last_name, security, quantity
FROM trades
INNER JOIN clients
on trades.client_id == clients.client_id
WHERE '2018-12-31' < trade_date AND trade_date < '2020-01-01'
ORDER BY trade_date
'''

## QUERY 08
sql_08 = '''
SELECT trade_date, trades.security, quantity, price
FROM trades
INNER JOIN price_history
ON trades.security == price_history.security
WHERE trades.client_id == 4 AND trades.trade_date == price_history.date
ORDER BY trade_date
'''

## QUERY 09
sql_09 = '''
SELECT trades.security, SUM(trades.quantity) AS quantity, price_history.price, SUM(trades.quantity) * price_history.price AS value
FROM trades
INNER JOIN price_history
ON price_history.security == trades.security
WHERE trades.client_id == 4 AND price_history.date == '2020-03-31'
GROUP BY trades.security
ORDER BY value DESC
'''

## QUERY 10
sql_10 = '''
SELECT trade_date, trades.security, quantity, post_price.price AS "purch. price", post_price.price*quantity AS cost, price_history.price AS "current price", price_history.price*quantity AS value
FROM ((trades
INNER JOIN price_history as "post_price"
ON post_price.security == trades.security AND post_price.date == trades.trade_date)
INNER JOIN price_history
ON price_history.security == trades.security)
WHERE price_history.date == '2020-03-31' AND trades.client_id == 4
ORDER BY trades.security
'''

################################################################################
if __name__ == '__main__':
    
    # obtain a database connection:
    #con = db.connect("./portfolio.db")
    
    # set some options to display enough columns of output
    #pd.set_option('display.width', 320)
    #pd.set_option('display.max_columns',10)
    
    
    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    #print(pd.read_sql(sql_08, con=con))
    #print()
    
    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    #print(pd.read_sql(sql_00, con=con))
    #print()
