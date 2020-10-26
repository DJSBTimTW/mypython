employee = {} #宣告字典
employee.setdefault('ename',[])
employee.setdefault('esalary',[])

print("--------------------")
print("員工薪資輸入")
print("若姓名處未輸入則代表結束")
print("--------------------")

name = input("請輸入姓名：")
while name != "":
    employee["ename"].append(name)
    esalary = input("請輸入薪資:")
    employee["esalary"].append(esalary) #同key多值
    print("")
    name = input("請輸入姓名：")

print("--------------------")
k=len(employee['ename']) #求ename裡面 值的總數
for key in range(0,k):
    print("員工{}的薪資為{}".format(employee['ename'][key], employee['esalary'][key]))
