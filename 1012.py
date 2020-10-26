# 列表生成式                 ※請一定要學會
# x = [0 for i in range(1,7)]                          # 設定 list 初值皆為0
# print(x)
# m = [i+1 for i in range(6)]                         # 設定 list 初值為1-6
# print(m)
# m = n = 3
# l = [[0 for i in range(m)] for j in range(n)]  # l = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(l)

# 使用 for 迴圈加總數字
# sum = 0
# n = int(input("請輸入欲加總的數字:"))
# for i in range(1, n+1):
#     sum += i                                         # sum = sum + i
# print(sum)

# 巢狀 for 迴圈
# for i in range(1,10):
#     for j in range(1,10):
#         print("{}x{}={:>2}".format(i, j, i*j), end=" ")
#     print()

# 後置 if 判斷式 ※請一定要學會
while True:
    grade = int(input("請輸入分數, 分數 0 則離開："))
    if grade==0: break
    flag = "及格" if grade >= 60 else "不及格"
    print(flag)
    print('{} 為 {}'.format(grade, "奇數" if grade % 2 else "偶數"))
