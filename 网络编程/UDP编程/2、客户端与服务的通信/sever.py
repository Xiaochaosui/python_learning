import socket

udpSever = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_self = '192.168.3.30'
port_self = 8081
udpSever.bind((ip_self,port_self))

while True:
    data,addr = udpSever.recvfrom(1024)
    print("客户端说:"+data.decode("utf-8"))
    dataSend = input("输入:")
    #print(addr,"///")
    udpSever.sendto(dataSend.encode("utf-8"),addr)

