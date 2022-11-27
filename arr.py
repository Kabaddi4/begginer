import pdb  #デバッグツール

arr = ["apple","orange","melon","graip"] 

arr.append("lemon") #追加
pdb.set_trace() #1つ下のコードのデバッグ
arr.insert(1, "peach")  #指定の場所へ追加
print(arr)