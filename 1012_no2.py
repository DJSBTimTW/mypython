employees=[]
employee={}
print("-----------------------\n員工薪資輸入\n若姓名處未輸入則代表結束\n-----------------------")
while True:
	empName=input("請輸入姓名:")
	if empName=="": break
	salary=int(input("請輸入薪資:"))
	employee["eName"]=empName
	employee["eSalary"]=salary
	employees.append(employee)
	employee={}
	print()
print("-----------------------")
for emp in employees:
	print("員工{}的薪資為{}".format(emp["eName"], emp["eSalary"]))
print()