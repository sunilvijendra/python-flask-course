def swap (x, y):
    return y, x;

def bubble_sort_1(inparr):
    arr = inparr
    for x in range(len(arr)):
        for y in range(len(arr)):
            if (arr[y] > arr[x]):
                temp = arr[x]
                arr[x] = arr[y]
                arr[y] = temp
    return arr

def bubble_sort_2(inparr):
    arr = inparr
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[y] > arr[x]:
                arr[x], arr[y] = swap(arr[x], arr[y])
    return arr

arr = []
n = int(input("Enter N: "))
for i in range(n):
    arr.append(int(input("Enter num: ")))
newarr = bubble_sort_2(arr)
print(newarr)
