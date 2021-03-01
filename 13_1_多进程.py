from random import randint
from time import time,sleep

def download_task(filename):
    print("开始下载%s..."%filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print("%s下载完成了！耗费了%d秒"%(filename,time_to_download))

def main():
    start = time()
    download_task("Python从入门到入土.pdf")
    download_task("PekingJOt.jpg")
    end = time()
    print("总共耗时%.2f秒"%(end-start))

if __name__ == '__main__':
    main(
