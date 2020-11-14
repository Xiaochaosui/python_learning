from multiprocessing import Process,Queue
import os,time

def write(q):
    print("启动写子进程---%s"%(os.getpid()))
    for char in ['A','B','C','D']:
        q.put(char)
        time.sleep(1)

    print("结束写子进程---%s"%(os.getpid()))

def read(q):
    print("启动读子进程---%s" % (os.getpid()))
    while True:
        value = q.get(True)
        print("value="+value)
    print("结束读子进程---%s" % (os.getpid()))


if __name__ == '__main__':
    # 父进程创建队列
    queue = Queue()

    pW = Process(target=write,args=(queue,))
    pR = Process(target=read,args=(queue,))
    pW.start()
    pR.start()
    pW.join()
    # pR进程里是个死循环，无法等待其结束,只能强行结束
    pR.terminate() # 强制结束进程
    print("父进程结束")
