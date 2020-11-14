import socket

ip_dest = '192.168.1.102'
port_dest = 8080
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip_dest,port_dest))
count = 0
while True:
    count += 1
    data = input("请输入给服务发送的数据：")
    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("服务器说:"+info.decode("utf-8"))
