from collections import Counter
a="aadcbffklsafksalfsaffanfsjnjksvodsv"
count=Counter(a)
print(count.items())
print(count.keys())
print(count.most_common())