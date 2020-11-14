import tkinter
import socket
import threading


def getInfo():
    while True:
        data = ck.recv(1024)
        dataStr = data.decode("utf-8")
        text.insert(tkinter.INSERT,dataStr)
ck = None
def connectSever():
    global ck
    ipStr = eIp.get()
    portStr = ePort.get()
    userStr = eUserName.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipStr,int(portStr)))
    client.send(userStr.encode("utf-8"))
    ck = client
    # 等待接收数据
    t = threading.Thread(target=getInfo)
    t.start()
def sendMail():
    global ck
    friend = eFriend.get()
    sendMessage = eSend.get()
    sendStr = eUserName.get()+":"+friend+":"+sendMessage
    ck.send(sendStr.encode("utf-8"))
    eSend.set("")

win = tkinter.Tk()
win.title("QQ客户端")
win.geometry("400x400+20+20")

labelUserName = tkinter.Label(win, text = "userName").grid(row=0,column = 0)
eUserName = tkinter.Variable()
entryUserName = tkinter.Entry(win,textvariable = eUserName).grid(row=0,column = 1)

labelIp = tkinter.Label(win, text = "ip").grid(row=1,column = 0)
eIp = tkinter.Variable()
eIp.set("192.168.1.102")
entryIp = tkinter.Entry(win,textvariable = eIp).grid(row=1,column = 1)

labelPort = tkinter.Label(win, text = "port").grid(row=2,column = 0)
ePort = tkinter.Variable()
ePort.set("8080")
entryPort = tkinter.Entry(win,textvariable = ePort).grid(row=2,column = 1)

button1 = tkinter.Button(win,text = "连接",command = connectSever).grid(row = 3,column = 0)




text = tkinter.Text(win,width = 30,height = 10)
text.grid(row = 4,column = 0)

eSend = tkinter.Variable()
entrySend = tkinter.Entry(win,textvariable = eSend).grid(row = 5,column = 0)

eFriend = tkinter.Variable()
entryFriend = tkinter.Entry(win,textvariable = eFriend).grid(row = 6,column = 0)

button2 = tkinter.Button(win,text = "发送",command =  sendMail).grid(row = 6,column = 1)

win.mainloop()