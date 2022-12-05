def judge(cat, dog, mix):
    if cat > mix or mix > cat + dog:
        return "NO"
    else:
        return "YES"
    
num1, num2 ,num3 = map(int, input().split())
ans = judge(num1, num2, num3)
print(ans)