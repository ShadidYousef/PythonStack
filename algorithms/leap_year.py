def isLeap(year):
    return 1 if year%100 == 0 or year%4 == 0 else 0
    
print(isLeap(2021))