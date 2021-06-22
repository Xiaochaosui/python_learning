import socket

ip_dest = '49.235.72.162'
port_dest = 20201
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip_dest,port_dest))

while True:
    str = input("请输入给服务发送的数据：")
    data = str +'\n'
    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("服务器说:"+info.decode("utf-8"))
