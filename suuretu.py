def equal(num_a, num_d, num_n):
    return (num_a + num_d) * num_n / 2

arr = [1, 5, 9, 13]

a = arr[0]
judge = arr[1]
judge2 = arr[2]
d = arr[-1]
n = len(arr)

if judge - a == judge2 - judge:
    ans = equal(a, d, n)
    print(ans)
else:
    print("null")