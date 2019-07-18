#!/usr/bin/python

import argparse

def find_max_profit(prices):
   # buy first day and set as initial buy
  buy = prices[0]
  # default to 0
  sell = 0

  for price in prices[1:]:
        if price < buy and sell < price:
              buy = price

        if buy < price and price > sell:
              sell = price

  max_profit = sell - buy
  return max_profit




Day1 = [10, 7, 5, 8, 11, 9] # / 6
Day2 = [100, 90, 80, 50, 20, 10] # / 10
find_max_profit(Day1)
find_max_profit(Day2)



if __name__ == '__main__':
      # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  
'''
=== Polya's PSP ===

1.What are they asking?
- Find the max profit from buying and selling within a list of days given diff prices
-
2. Plan of attack!
- Look through the days and see which day we can get the lowest price of stock and buy
- call that initial_buy
- look through the days after the initial buy and find the best profit
  - Profit = initial bought stock - current stock price
  - if in negative then there was no profit so move onto the next day to check
- Once a positive profit has been determined lets save as profit
- look thorough days after and compare profits and if they are less than current profits
  then keep our sell date if not then lets sell that day instead
- continue this thru the length of days(data) given

3. Execute plan
- Start cranking out code!

4. Review, extend,improve refactor?


'''