import socket
import sys

if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(u"创建socket实例失败")
        print(u"原因: %s" % str(err))
        sys.exit();

    print(u"socket实例创建成功!")

    HOST = input(u"输入目标主机: ")
    PORT = input(u"输入目标主机端口: ")

    try:
        sock.connect((HOST, int(PORT)))
        print(u"Socket已经连接上目标主机： %s ，连接的目标主机端口: %s" % (HOST, PORT))
        sock.shutdown(2)
    except socket.error as err:
        print(u"连接主机：%s 端口：%s 失败！" % (HOST, PORT))
        print(u"原因: %s" % str(err))
    sys.exit();
