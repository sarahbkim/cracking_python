# array_stock_picker
arr = [100, 300, 50, 500, 40, 1000]
def array_stock_picker(arr):
    for i, amt in enumerate(arr):
        buy_time = i
        sell_time = i+1
        if(i+2<len(arr)):
            if arr[i+1] < arr[buy_time]:
                buy = i+1
            if arr[i+2] > arr[sell_time]:
                sell_time = i+1
        else: 
            break;
    profit = arr[sell_time] - arr[buy_time]
    print(buy_time, sell_time, profit)
            
# array_stock_picker(arr).should==[4, 5, 960]
array_stock_picker(arr)

def get_best_profit(stock_prices_yesterday):
    min_price = stock_prices_yesterday[0]
    max_profit = 0
    for current_price in stock_prices_yesterday:
        min_price = min(min_price, current_price)
        max_profit = max(max_profit, current_price - min_price)
    return max_profit


# greedy "algorithm" -- get product of all numbers in array besides current index
def get_products_besides_index(arr):
    # make array to hold product
    products = [1] * len(arr)

    # get all amounts after

    # get all amounts before and multiply

    return products
