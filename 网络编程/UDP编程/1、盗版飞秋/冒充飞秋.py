'''
TCP：简历可靠的连接，并且通信双方都可以以流的形式发送数据相对于TCP，UDP则是面向无连接的协议

使用UDP协议时，不需要知道对方的IP地址和端口号就可以发送数据包，但是能不能到达就不知道了

虽然UDP传输数据不可靠，但他的优点时比TCP速度快，对于要去不高的数据可以使用UDP
'''
import socket

ip_dest = ''
port_dest = 8080
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dataSend = 'xcs is a good man'
udp.bind((ip_dest,port_dest))
udp.sendto(dataSend.encode("utf-8"),(ip_dest,port_dest))