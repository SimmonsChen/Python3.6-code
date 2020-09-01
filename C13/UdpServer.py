import socket

MAX_SIZE = 5600
# 新建socket连接
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定主机和端口，主机为空表示任意主机
sock.bind(('localhost', 8005))

while True:
    print(u'服务器等待连接...')
    # 当有连接时，将接收到的数据存到data中，远程连接细节保存到address中
    # MAX_SIZE表示可接收最长为5600字节的信息
    data, address = sock.recvfrom(MAX_SIZE)
    data = data.decode()
    resp = "UDP服务器在发送数据"
    # 发送数据包
    sock.sendto(resp.encode(), address)
