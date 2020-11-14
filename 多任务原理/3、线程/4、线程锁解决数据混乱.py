'''

两个线程同时工作，一个存钱，一个取钱

加锁

'''

import threading

lock = threading.Lock()

num = 0
def run(n):
    global num
    # 锁
    # 确保了这段代码只能有一个线程从头到尾得完整执行
    # 阻止了多线程得并发执行，包含锁得某段代码实际上只能以单线程模式执行，所以效率大大降低了
    # 由于它可以存在多个锁，而且不同线程持有不同得锁，并且试图获得其他得锁，可能造成死锁，导致多个线程挂起，只能操作系统强制终止
    '''lock.acquire()
    try:
        for i in range(100000000):
            num = num + n
            num = num - n
    finally:
        # 修改完一定要释放锁
        lock.release()'''

    # 与上面代码功能相同.with lock 可以自动上锁与解锁
    with lock:
        for i in range(100000000):
            num = num + n
            num = num - n







if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=(2,))
    t2 = threading.Thread(target=run,args=(7,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num = ",num)