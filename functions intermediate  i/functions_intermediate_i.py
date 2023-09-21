import random

def randInt(min_val=0, max_val=100):
    if max_val < 0:
        return "max value cannot be less than 0"
    elif min_val > max_val:
        print("max value was smaller than min so they got swapped!")
        min_val, max_val = max_val, min_val
    return round(random.random() * (max_val - min_val) + min_val)

print(randInt())
# print(randInt(max_val=50))
# print(randInt(min_val=50))
# print(randInt(min_val=50,max_val=500))