def aaaaaa():
    print("還敢下來阿冰鳥")
aaaaaa()

def getarea(width,height):
    area=width*height
    return area

# w=int(input("input width:"))
# h=int(input("input height:"))
# result=getarea(w,h)
# print("this area is {}".format(result))

# def mysum(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total

# print(mysum(1, 2, 3, 4,5,6))

def bmi(height, weight, isround=True): 
    return round(weight / (height / 100) ** 2, 2) if isround else weight / (height / 100) ** 2

print(bmi(175, 80))                                # 需依照函式的參數順序給值
print(bmi(175, 80, False))                     # 若結果不要四捨五入，則第3個參數給False
print(bmi(weight=80, height=175))       # 直接給參數名稱與值，可避免參數順序錯誤的問題