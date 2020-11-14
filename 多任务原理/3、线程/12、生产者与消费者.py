import threading
import queue,time,random

# 生产者
def product(id,q):
    while True:
        num = random.randint(0,1000)
        q.put(num)
        print("生产者%d生产了%d数据放入了队列"%(id,num))
        time.sleep(3)
        # 任务完成
    q.task_done()

# 消费者
def customer(id,q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者%d从队列中消费了%d数据"%(id,item))
        time.sleep(3)
        # 任务完成
    q.task_done()



if __name__ == '__main__':
    # 消息队列
    q = queue.Queue()
    # 启动生产者
    for i in range(5):
        t= threading.Thread(target=product,args=(i,q))
        t.start()

    # 启动消费者
    for i in range(3):
        t= threading.Thread(target=customer,args=(i,q))
        t.start()