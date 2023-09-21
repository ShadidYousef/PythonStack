#1
def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i]="big"
    print(arr)

biggie_size([-1, 3, 5, -5])

#2
def count_positives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count+=1
    # arr.pop()
    # arr.append(count)
    arr[len(arr)-1]=count
    print(arr)

count_positives([1,6,-4,-2,-7,-2])

#3
def sum_total(arr):
    arrSum = 0
    for i in range(len(arr)):
        arrSum+=arr[i]
    return arrSum

print(sum_total([1,2,3,4]))

# OR 
def sum_total_v2(arr):
    return sum(arr)

print(sum_total_v2([1,2,3,4]))

#4
def arr_average(arr):
    return sum(arr)/len(arr)

print(arr_average([1,2,3,4]))

#5
def length(arr):
    return len(arr)

print(length([37,2,1,-9]))

#6
def minimum(arr):
    for i in range(len(arr)):
        if len(arr) == 0:
            return False
        else:
            return min(arr)
        
print(minimum([37,2,1,-9]))

#7
def maximum(arr):
    for i in range(len(arr)):
        if len(arr) == 0:
            return False
        else:
            return max(arr)
        
print(maximum([37,2,1,-9]))

#8
def ultimate_analysis(arr):
    analysis = {}
    analysis['arrSum'] = sum(arr)
    analysis['average'] = sum(arr) / len(arr)
    analysis['minimum'] = min(arr)
    analysis['maximum'] = max(arr)
    analysis['length'] = len(arr)
    return analysis

print(ultimate_analysis([37,2,1,-9]))

#10
def reverse_list(arr):
    left=0
    right=len(arr)-1
    for i in range(len(arr)):
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    return arr

print(reverse_list([37,2,1,-9]))