def keisan(num):
    return int(num) * 1.4   #引数をintで囲んでから行う

output = input("数字を入力してください：")
ans = keisan(output)
print(ans)