num=int(input("請輸入星星數量:"))
numa=int((num+1)/2) #奇數星星三角形 (總星數+1)/2=行數
for i in range(1,numa+1,1): #i控制星星數量 故從1開始 條件從1到行數並以+1為變量
    for ia in range(numa-i):
        print(" ",end="")
    for ib in range(2*i-1): #當前行數2倍-1 奇數對稱 例如第2行印2*2-1=3
        print("*",end="")
    print("")

for j in range(numa-1,0,-1): #上半最後一行為正中間 故從總行數-1開始並以-1為變量
    for ja in range(numa-j):
        print(" ",end="")
    for jb in range(2*j-1):
        print("*",end="")
    print("")