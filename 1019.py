# def scope():
#     global var1
#     var1 = 1
#     print(var1, var2)
# var1=10
# var2=20
# scope()
# print(var1,var2)

# 使用亂數模組隨機取得 1-42 之間的整數
import random
help(random.randint)
print(random.randint(1, 42))
# 省略寫法
from random import randint
randint(1, 42)
# 使用時間模組取得目前的日期時間
import time
print(time.strftime("%Y.%m.%d %H:%M:%S"))

from datetime import datetime
print(datetime.now())
# 使用作業系統模組清除目前提示字元的畫面
import os
os.system("cls")
# 多個模組可以合併為一行引用
import random, time, os
