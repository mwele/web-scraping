stocks = {"GOOG": (613.30, 625.86, 610.50),
"MSFT": (30.25, 30.70, 30.19)}
for stock, value in stocks.items():
	print("{} last value is {}".format(stock,value[0]))

fruits={"apples":(92,43,"from usa"),
          "mangoes":(909,909,"from kenya")}
print(fruits.keys(), fruits.values())
for fruit in fruits.items():
	print("{}are from {}".format(fruits,value[2]))