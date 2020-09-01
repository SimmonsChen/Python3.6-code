##def w1(func):
##    def inner():
##        print('额外功能')
##        return func()
##    return inner
##
##@w1
##def f1():
##    print('本来功能')
##
##f1()


##def AddCheck(func):
##    def check(*args,**kw):
##        print('真的要操作数据吗？')
##        return func(*args,**kw)
##    return check
##
##@AddCheck
##def f1(arg1):
##    print('增加数据'+arg1)
##@AddCheck 
##def f2(arg1,arg2):
##    print('删除数据'+arg1+arg2)
##@AddCheck
##def f3(arg1,arg2,arg3):
##    print('修改数据'+arg1+arg2+arg3)
##
##f1('学生1')
##f2('学生1','班级1')
##f3('学生1','班级1','学校1')


def d1(func):
    def check(*args,**kw):
        print('真的要操作数据吗？')
        return func(*args,**kw)
    return check
def d2(func):
    def check2(*args,**kw):
        print('真的是该部门吗？')
        return func(*args,**kw)
    return check2

@d1
@d2
def f1(arg1):
    print('增加数据'+arg1)

f1('部门1')
