from multiprocessing import Process
from time import sleep
"""
Ping Pong各输出了十个，因为创建子进程的时候，
子进程复制了父进程所有的数据集结构，所以各有一个counter变量
"""

counter = 0

def sub_task(string):
    global counter
    while counter < 10:
        print(string, end=" ", flush=True)
        counter += 1
        sleep(0.01)

def main():
    Process(target=sub_task,args=("Ping",)).start()
    Process(target=sub_task,args=("Pong",)).start()

if __name__ == "__main__":
    main()