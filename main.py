# name = "jojo"
# print("hello ,"+name)


# iNum=int(input("0~9:"))
# if 4> iNum >2:
#     print("*"*30)
# else:
#     print("*"*10)

# sid=input("請輸入您的學號：")                 # 假設輸入 9A310637
# sname=input("請輸入您的姓名：")           # 假設輸入 王大明
# dage=int(input("請輸入您的年齡："))       # 假設輸入 20, 要透過 int() 才是整數型別

# print(sid+"\n"+sname+"\n"+str(dage))       # \n 代表換行的意思，與 C 語言的逸脫字元相當
# print(sid, sname, dage, sep="\n")        

# list (串列)
garagelist =  ["Benz", "BMW", "Rolls-Royce"]
# for eachcar in garagelist:
#     print(eachcar)                    # for 無須括弧，但須 4 個空白表示縮排

# tuple (序列、元組) 其內容一經設定之後不可更改
garagetuple = ("Honda", "Toyota", "Nissan")
# for eachcar in garagetuple:
#     print(eachcar)

# 取用 list 或 tuple
# print(garagelist[0])
# print(garagetuple[1])
# print(garagelist[3])                  # 超出索引範圍
# print(garagelist[0:2])               # 從註標 0 開始取出 2 個元素(slice切片)

# 取出 list 或 tuple 所有元素，並以 > 作為分隔符號
# for eachcar in garagetuple:    # 以迴圈取出所有元素，更改換行字元為 >
#     print(eachcar, end=" > ")
# print(*garagetuple, sep=" > ")  # 取出所有元素，指定 > 作為分隔符號
# print(" > ".join(garagetuple))    # 以字元 > 作為每個元素 join 在一起的分隔符號

# 更改 list 元素值
#garagelist[2]="Bentley"
# 更改 list 元素值並提示輸入其他廠牌
#garagelist[2]=input("Please input your car brand : ")
# 更改 tuple 元素值，但會失敗，說明了 tuple 元素的值一經設定後就不能更改
#garagetuple[2]="Mitsubishi"

# 增加 list 元素值
# garagelist.append("Porsche")
# 將一個已存在的 list或tuple 增加至目前的 list 中
# garagelist.extend(garagelist)
garagelist.extend(garagetuple)
# 插入 list 元素至指定位置
# garagelist.insert(1, "Ferrari")

# 
# print(garagelist[2:5])

# 反轉 list 元素的位置
# garagelist.reverse()
# 排序 list 中所有元素
# garagelist.sort()
# sortedList = sorted(garagelist)
# 刪除 list 中某個元素值
# garagelist.remove("Honda")
# 刪除並回傳 list 中最後一個元素
# garagelist.pop()
# 刪除並回傳 list 中註標為1的元素
# garagelist.pop(1)
# 刪除整個 list 變數
# del garagelist
# print(" > ".join(garagelist))    # 以字元 > 作為每個元素 join 在一起的分隔符號

# dict 設定，使用大括弧，每個元素須以【鍵:值】方式以逗號隔開
student = {'sid':'9A136740', 'sname':'Peter', 'age':20}
# dict 取用指定鍵之值
# print(student["sid"])                                         # 若不存在會出現 KeyError 的錯誤
# print(student.get("sid",999))                              # 建議用此方式
# dict 取用指定鍵之值，若此鍵不存在，則立刻新增相關鍵值
# print(student.setdefault("sid","9A543328"))  # 已有 sid 欄位，因此不會新增
# print(student)
# print(student.setdefault("sex",1))
# print(student)
# msg="This is a book."
# countdict={}
# for ch in msg:
#     countdict.setdefault(ch, 0)       # 將首次找到的key，其 value 設為 0
#     # print(countdict)
#     # input()
#     countdict[ch]=countdict[ch]+1
#     print(countdict)

# 取得 dict 以鍵為組合的 dict_keys 物件
print(student.keys())
# 取得 dict 以值為組合的 dict_values 物件
print(student.values())
# 取得 dict 以鍵, 值組合的 dict_items 物件
print(student.items())
