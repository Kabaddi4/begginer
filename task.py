a, b, x = map(int, input().split())

ab = a + b
if a > x or x > ab:
    print("NO")
else:
    print("YES")
