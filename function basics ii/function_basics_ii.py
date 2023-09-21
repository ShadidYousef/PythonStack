#1
def countdown(num):
    arr = []
    for i in range(num,-1,-1):
        arr.append(i)
    return arr

print("\n#1\n","#"*20,"\ncountdown:",countdown(5))

#2
def print_and_return(arr):
    print("\n#2\n","#"*20,"\nthis is the print value:", arr[0])
    return arr[1]

test = print_and_return([1,2])
print("this is the return value:", test)

#3
def first_plus_length(arr):
    return arr[0]+len(arr)

print("\n#3\n","#"*20,"\nfirst plus length:",first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(arr):
    if len(arr) <= 2:
            return False
    newList = []
    for i in range(0,len(arr),1):
        if arr[i] > arr[1]:
            newList.append(arr[i])
    print("\n#4\n","#"*20,"\nthe values number is:",len(newList))
    print("new list is:",newList)

values_greater_than_second([5,2,3,2,1,4])

#5
def length_and_value(size,value):
    mylist = []
    for i in range(size):
        mylist.append(value)
    print("\n#5\n","#"*20,"\nlength and value:",mylist)

length_and_value(6,2)