def equal(num_a, num_d, num_n):
    return (num_a + num_d) * num_n / 2

def arr_equal(num_a, num_d, num_n):     #等差数列の和(numpy range)
    return (num_a + num_d) * num_n / 2

arr = [1, 5, 9]     
a = arr[0]
judge_1 = arr[1]
d = arr[-1]
n = len(arr)    #要素数

if judge_1 - a == d - judge_1:
    ans = arr_equal(a, d, n)
    print(ans)
else:
    print("null")
