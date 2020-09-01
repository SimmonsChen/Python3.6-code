##a=10
##b=0
##c=a/b
##print(c)


##def TestError(d):
##     try:
##         print('正确结果:',8/d)
##     except ZeroDivisionError:
##         print("抛出一个除0异常")
##     else:
##         print('其他问题!')
##     finally:
##         print ('异常终结者')
##
##i=4
##while(i>=0):
##    TestError(i)
##    i-=2
##
##

##while True:
##    s = input('请输入一个整数：')
##    try:
##      i = int(s)
##      i = 8/i
##    except(ValueError,ZeroDivisionError) as err:
##        print(err)
##    else:
##        print('正确！')
##

##a=10
##b=0
##if(b==0):
##    raise ZeroDivisionError('0不能被除啊')
##print("good")



##class TestError(Exception):
##        def __init__(self, err='数据库错误'):
##            Exception.__init__(self,err)
##
##raise TestError


import pdb
# 九九乘法表
for i in range(1, 10):
        for j in range(1, i+1):
            pdb.set_trace()
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()














