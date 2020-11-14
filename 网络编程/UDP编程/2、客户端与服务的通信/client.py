import socket

ip_dest = '192.168.1.102'
port_dest = 8081
udpClient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#udpClient.bind((ip_dest,port_dest))
while True:
    dataSend = input("输入:")
    udpClient.sendto(dataSend.encode("utf-8"),(ip_dest ,port_dest))
    dataRecv=udpClient.recv(1024)
    print("服务器说:"+dataRecv.decode("utf-8"))