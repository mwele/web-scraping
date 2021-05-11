from collections import namedtuple
Stock=namedtuple("stock","Symbol current high low")
stock=Stock("FB", 75.00, high=75.03, low=74.90)
print(stock.high)
Symbol, current,high,low=stock
print(current)
print(low)
print(Symbol)
print("______________________________________")

stocks = {"GOOG": (613.30, 625.86, 610.50),
"MSFT": (30.25, 30.70, 30.19)}

print(stocks)
#print(help(stocks))
print("GOOG IS: ", stocks.get("GOOG"))