import socket
from time import ctime

HOST = 'localhost'
PORT = 5008
BUF_SIZE = 1024
ADDRESS = (HOST, PORT)

if __name__ == '__main__':
    # 新建socket连接
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将套接字与指定的ip和端口相连
    server_socket.bind(ADDRESS)
    # 启动监听，并将最大连接数设为5
    server_socket.listen(5)
    print("[***] 正在监听: %s:%d" % (HOST, PORT))
    # setsocketopt()函数用来设置选项，结构是setsocketopt(level, optname, value)
    # level定义了哪个选项将被使用，通常是SOL_SOCKET,意思是正在使用的socket选项。
    # socket.SO_REUSEADDR表示socket关闭后，本地端用于该socket的端口号立刻就可以被重用。
    # 通常来说，只有经过系统定义一段时间后，才能被重用。
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        print(u'服务器等待连接...')
        # 当有连接时，将接收到的套接字存到client_sock中，远程连接细节保存到address中
        client_sock, address = server_socket.accept()
        print(u'连接客户端地址: ', address)
        while True:
            # 打印客户端发送的消息
            data = client_sock.recv(BUF_SIZE)
            if not data or data.decode('utf-8') == 'END':
                break
            print("来自客户端信息: %s" % data.decode('utf-8'))
            print("发送服务器时间给客户端: %s" % ctime())
            try:
                # 发送时间
                client_sock.send(bytes(ctime(), 'utf-8'))
            except KeyboardInterrupt:
                print("用户取消")
        # 关闭客户端socket
        client_sock.close()
    # 关闭socket
    server_socket.close()