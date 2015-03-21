import unittest

def max_profit(arr):
  """ stock price array needs to be at least of len 2 """
  buy = arr[0]
  sell = arr[1]
  profit = sell - buy

  i = 0
  while i < len(arr[1:]):
    buy = min(arr[i], buy)
    sell = max(arr[i+1], sell)
    #profit = max(profit, sell-buy)
    i += 1

  return sell-buy
  

class StocksTest(unittest.TestCase):

    def test(self):
      stock_arr = [10, 30, 40, 4, 100, 30]
      self.assertEqual(max_profit(stock_arr), 96)

      stock_arr_2 = [50, 40, 100, 1, 1000]
      self.assertEqual(max_profit(stock_arr_2), 999)


if __name__ == '__main__':
    unittest.main()