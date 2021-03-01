import time                                                                           
"""
上面那样循环会堵塞输出,要等sleep全部执行完,才一并打印出全部结果。
要在for循环里面的end = ""后面加上flush = True
"""


print("没有flush效果")
time.sleep(0.5)

print("Loading",end = "")
for i in range(6):
    print(".",end = '')
    time.sleep(0.2)

print("有flush效果")

print("Loading",end = "")
for i in range(6):
    print(".",end = '', flush=True)
    time.sleep(0.2)