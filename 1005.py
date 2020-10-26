student = {'sid':'9A136740', 'sname':'Peter', 'age':20}
# dict 取用指定鍵之值
# print(student["sid"])                                         # 若不存在會出現 KeyError 的錯誤
# print(student.get("sid",999))                              # 建議用此方式
# dict 取用指定鍵之值，若此鍵不存在，則立刻新增相關鍵值
# print(student.setdefault("sid","9A543328"))  # 已有 sid 欄位，因此不會新增
# print(student.setdefault("sex",1))
# for key in student:                                   # 方法2
#     print('{}: {}'.format(key, student[key]))
# if "si" in student: 
#     print(student["si"])
# else:
#     print("404")
#     student["si"]=0
# print(student)
# print(len(student))
# 複製整個 dict
# studentdict = student.copy()
# print(student)
# 增加 dict 元素
# student["phone"]="0936-279195"
# 修改 dict 指定元素
# student["phone"]="0901-179195"                 # 若不存在，會變成新增
# student.update({"sname":"Tom", 'age':30})
# print(student)
# input()
# 刪除 dict 指定元素
# del student["phone"]
# input()	                       # 若不存在會出現 KeyError 的錯誤
# student.pop("phone")
# print(student)
# 清空 dict 所有元素
# student.clear()
# 刪除整個 dict
# del student
# num=3
# print("num變數地址:",id(num))
# print("student變數地址:",id(student))
# varA=3
# varA=student
# print(id(varA))
# varB=3
# varB=student
# varB=student.copy()
# print(id(varB))

# varA = 666
# print(type(varA))
# varB = [123, "456"]
# print(type(varB))

# if not 'student' in dir():
#     print('變數未定義')
# else:
#     if not student:
#         print('變數為空值')
#     else:
#         print('\n'.join(['%s: %s' % (key, value) for (key, value) in student.items()]))
# print(dir())

for i in [1,2,3,4,5,6,7,8,9,10]: print(i, end=" ")