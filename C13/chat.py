import socket
import sys
import argparse

HOST = '127.0.0.1'
PORT = 8080


def listen_socket(host, port):
    """ 监听socket TCP连接 """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口，host为'',表示监听所以端口
    sock.bind((host, port))
    # 监听最大连接数
    sock.listen(100)
    return sock


def receive_msg(sock):
    """ 解析数到数据 """
    data = bytearray()
    msg = ''
    # 以及字节存储
    while not msg:
        recv = sock.recv(4096)
        if not recv:
            # 关闭socket
            raise ConnectionError()
        data = data + recv
        if b'\0' in recv:
            # 判断收到数据，'\0'一直是最后的那个特征值。
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg


def prep_msg(msg):
    """ 发送消息 """
    msg += '\0'
    return msg.encode('utf-8')


def send_msg(sock, msg):
    """ 准备发送消息"""
    data = prep_msg(msg)
    sock.sendall(data)


def handle_client(sock, addr):
    """ 接收客户端数据并回复 """
    try:
        msg = receive_msg(sock)  # 完成数据的接收
        print('{}: {}'.format(addr, msg))
        send_msg(sock, msg)  # 发送数据
    except (ConnectionError, BrokenPipeError):
        print('Socket错误')
    finally:
        print('与{}连接关闭'.format(addr))
        sock.close()


def server():
    listen_sock = listen_socket(HOST, PORT)
    addr = listen_sock.getsockname()
    print('正在监听：{}'.format(addr))
    while True:
        client_sock, addr = listen_sock.accept()
        print('连接来自： {}'.format(addr))
        handle_client(client_sock, addr)

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    while True:
        try:
            print('\n已经连接{}:{}'.format(HOST, PORT))
            print("输入信息, 按‘enter’发送, 'q'键取消")
            msg = input()
            if msg == 'q': break
            send_msg(sock, msg)
            print('发送消息: {}'.format(msg))
            msg = receive_msg(sock)
            print('收到回复: ' + msg)
        except ConnectionError:
            print('Socket错误')
            break

        finally:
            sock.close()
            print('关闭连接\n')


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='聊天小应用')
    parser.add_argument('role', choices=choices, help='选择角色：client ,或者 server。')
    args = parser.parse_args()
    execute = choices[args.role]
    execute()
