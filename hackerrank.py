
n = int(input())
arr = map(int,input().split())
lst=[]
for i in arr:
    lst.append(i)

lst.sort(reverse=True)
print(lst[2])
############################################
from collections import Counter
if __name__ == '__main__':
    n = int(raw_input())
    arr = list(set(map(int, raw_input().split())))
    arr.sort()
    print arr[-2]