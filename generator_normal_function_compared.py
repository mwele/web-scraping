


#import sys

import sys
nums_squared_lc = [i * 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))

'''In this case, the list you get from the list comprehension is 87,624 bytes, while the generator object is only 120. This means that the list is over 700 times larger than the generator object!'''
