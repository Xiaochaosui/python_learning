import socket
import threading
def run(ck,addr):
    data = ck.recv(1024)
    print("收到" + str(addr) + "的数据：" + data.decode("utf-8"))
    #sendData = input("请输入返回给客户端的数据：")
    ck.send("sendData:xcs is a good man!".encode("utf-8"))

#创建一个socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_self = '192.168.1.102'
port_self = 8080
# 绑定IP端口
server.bind((ip_self,port_self))
# 监听
server.listen(5)
print("服务器启动成功......")

while True:
    # 等待连接
    clientSocket, clientAddress = server.accept()

    t = threading.Thread(target=run,args=(clientSocket,clientAddress))
    t.start()





    '''data = clientSocket.recv(1024)
    print("收到"+str(clientAddress)+"的数据："+data.decode("utf-8"))
    sendData = input("请输入返回给客户端的数据：")
    clientSocket.send(sendData.encode("utf-8"))'''
