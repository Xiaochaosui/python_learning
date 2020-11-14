'''

客户端：创建TCP连接时，主动发起连接的一方
服务器：被连接一方
1、创建一个socket
:参数1：指定协议，AF_INET或 AF_INET6分别表示IPv4与6
:参数2：socket.SOCK_STREAM 执行使用面向流的TCP协议
2、建立连接
:参数：是一个元组，第一个元素为要连接的IP地址，第二个参数为端口
3、等待接收数据
4、断开连接
'''
import socket
# 创建一个socket
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
ip_dst = "www.sina.com.cn"
port_dst = 80
header_send = b'GET / HTTP /1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'
sk.connect((ip_dst,port_dst))
sk.send(header_send)
#  等待接收数据
data = []
while True:
    # 每次接收1k的数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break
dataStr = (b''.join(data)).decode("utf-8")

# 断开连接
sk.close()
#print(dataStr)
headers,html = dataStr.split("\r\n\r\n")
print(html)