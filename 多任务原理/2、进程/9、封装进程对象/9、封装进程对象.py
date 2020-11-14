from xcsProcess import XcsProcess


if __name__ == '__main__':
    print("父进程启动")
    # 创建子进程
    p = XcsProcess("test")
    # 自动调用进程对象的run方法
    p.start()
    p.join()
    print("父进程结束")