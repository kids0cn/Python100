"""
多个线程共享程序资源，包括全局变量
多个线程对同一资源进行竞争使用时，如果没有上保护，会出现混乱
"""

from time import sleep
from threading import Thread

class Account(object):
    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟受理存款需要0.01秒
        sleep(0.01)
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance
    

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._acount = account
        self._money = money

    def run(self): # 启动线程时，自动运行这个命令
        self._acount.deposit(self._money)
        print("启动了")

def main():
    account = Account() # 实例化了一个account
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()