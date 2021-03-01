from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' %filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target = download_task,args=("Ironman.mp4",))
    p2 = Process(target = download_task,args=("SpiderMan.avi",))

    p1.start() # Process的start()方法用来启动进程
    p2.start()
    p1.join()
    p2.join()   # join用来等待进程结束才执行后面的语句
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

