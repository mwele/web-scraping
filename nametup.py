from collections import namedtuple
stock=namedtuple("stock","symbol current high low" )
stock=stock("FB",75.0,high=75.03,low=74.0)
print(stock.symbol)
print(stock.current)
print(stock.high)
print(stock.low)

