times=int(input(""))
sp=int(times/2)
for i in range(1,times+1,2):
    print(" "*sp,end="")
    print("*"*i)
    sp-=1
sp=1
for u in range(times-2,0,-2):
    print(" "*sp,end="")
    print("*"*u)
    sp+=1
