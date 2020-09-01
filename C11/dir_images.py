import os
import shutil
import time

# 可选的图片列表
IMG = ['jpg', 'jpeg', 'gif', 'png']

# 重命名图片及删除非图片文件
def rename_image(path):
    global i  # 定义全局变量
    if not os.path.isdir(path) and not os.path.isfile(path):  # 判断是否是目录或文件
        return False
    if os.path.isfile(path):  # 如果是文件
        file_path = os.path.split(path)  # 分割出目录与文件名
        lists = file_path[1].split('.')  # 分割出文件与文件扩展名
        file_ext = lists[-1]  # 取出后缀名
        if file_ext in IMG:  # 判断该后缀名是否是图片的后缀名
            os.rename(path, file_path[0] + "/" + lists[0] + str(i) + '.' + file_ext)
            i += 1
        else:
            print(file_path)
            os.remove(os.path.join(file_path[0], file_path[1]))
    elif os.path.isdir(path):  # 如果是目录
        for x in os.listdir(path):  # 递归重命名程序
            rename_image(os.path.join(path, x))


# 创建文本索引文件
def create_index(path):
    if not os.path.isdir(path) and not os.path.isfile(path):  # 判断是否是目录或文件
        return False
    if os.path.isdir(path):
        lists = os.listdir(path)
        with open(os.path.join(path, 'index.txt'), 'a+', encoding='utf-8') as f:
            for item in lists:
                f.write(item)
                f.write("\n")


# 压缩目录下的文件
def archive_dir(path):
    shutil.make_archive(path, 'zip')


# 执行主函数
def main(path):
    rename_image(path)
    create_index(path)
    archive_dir(path)


if __name__ == "__main__":
    img_dir = input("请输入路径:")   # 取得图片文件夹路径, 比如"E:\images"
    start = time.time()  # 计时
    i = 0  # 初始化计算器i为0
    main(img_dir)
    m = time.time() - start
    print("程序运行耗时:%0.2f" % m)
    print("总共处理了%d张图片" % i)
