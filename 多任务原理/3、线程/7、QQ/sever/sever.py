import tkinter
import socket
import threading

win = tkinter.Tk()
win.title("QQ服务器")
win.geometry("400x400+20+20")

users = {}


def run(ck,ca):
    userName = ck.recv(1024).decode("utf-8")
    users[userName] = ck
    print(users)
    while True:
        rData = ck.recv(1024)
        dataStr = rData.decode("utf-8")
        infolist = dataStr.split(":")
        sendStr = infolist[0]+":"+infolist[2]+"\n"
        users[infolist[1]].send(sendStr.encode("utf-8"))



def start():
    ipStr = eIp.get()
    portStr = int(ePort.get())
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP端口
    server.bind((ipStr, portStr))
    # 监听
    server.listen(10)
    printStr = "服务器启动成功......"
    text.insert(tkinter.INSERT,printStr)
    while True:
        # 等待连接
        ck, ca = server.accept()
        t = threading.Thread(target=run, args=(ck, ca))
        t.start()

def startSever():
    s = threading.Thread(target=start)
    s.start()



labelIp = tkinter.Label(win, text = "ip",font = ("黑体",20),).grid(row=0,column = 0)
labelPort = tkinter.Label(win, text = "port",font = ("黑体",20),).grid(row=1,column = 0)
# 绑定变量 文本编辑框
eIp = tkinter.Variable()
eIp.set("192.168.1.102")
ePort = tkinter.Variable()
ePort.set("8080")
entryIp = tkinter.Entry(win,textvariable = eIp).grid(row=0,column = 1)
entryPort = tkinter.Entry(win,textvariable = ePort).grid(row=1,column = 1)

buton = tkinter.Button(win,text = "启动",command = startSever).grid(row=2,column = 0)

text = tkinter.Text(win,width = 30,height = 10)
text.grid(row = 3,column = 0)


win.mainloop()