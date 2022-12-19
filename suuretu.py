arr = [1, 5, 9]

a = arr[0]
middle = arr[1]
d = arr[2]
n = len(arr)

if middle - a == d - middle:
    print("equal")
    print(n)
else:
    print("null")