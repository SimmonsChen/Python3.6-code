import socket

MAX_SIZE = 5600
# 新建socket连接
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MESSAGE = "UDP服务器，你好！[握手中...]"

if __name__ == "__main__":
    # 输入主机
    HOST = input(u"输入目标主机: ")
    # 输入端口
    PORT = int(input(u"输入目标主机端口: "))
    # 发送数据包
    sock.sendto(MESSAGE.encode(), (HOST, PORT))
    data, address = sock.recvfrom(MAX_SIZE)
    print("来自UDP的回复:")
    print(repr(data.decode()))
