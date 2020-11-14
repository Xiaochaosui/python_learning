from multiprocessing import Process
from time import sleep
num = 100
def f():
    print("启动子进程")
    global num # -> num = 100
    num += 1
    print(num)
    sleep(3)
    print("子进程结束")



if __name__ == '__main__':
    print("父进程开始")
    p1 = Process(target=f)
    p1.start()
    p1.join()

    p2 = Process(target=f)
    p2.start()
    p2.join()
    # 在子进程中修改全局变量对父进程的全局变量无影响
    # 在创建子进程时对全局变量做了一个备份，父进程中的与子进程的num完全不一样
    print("父进程结束---%d"%(num))