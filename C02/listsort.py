stu1=['10001','男','张晓光'];
stu1.sort()
print('学生：',stu1)

score1=[80,100,98,59] # 列表中是单一的数据类型，直接使用sort(),默认升序
score1.sort(); 
print('成绩1：',score1)
score2=score1
score2.sort(reverse =True)
print('成绩2：',score2) 
score3= score2[:]
score3.sort()
print('成绩3：',score3)
print('位置：',id(score1),id(score2),id(score3))
#列表排序#
stu1=['10001','男','张晓光'];
stu1.sort(key=len)   # keys是带参数的函数，定义排序过程中调用函数，用于每个元素提取比较值，默认为None 
print('学生：',stu1)
#将数字转换成“0”， 保持最小值，
stu1=['10001','男','张晓光',20.0];
def comp(x):
    if type(x) is not  str:
        return '0'
    else:
        return x

stu1.sort(key=comp)
print('学生：',stu1)
#删除列表#
stu1=['10001','男','张晓光'];
del stu1[0]
del stu1[-1]
del stu1[0:3]
print('学生：',stu1)        # 学生： ['男']
#获取最大最小值以及长度#
score1=[80,100,98,59]
print ('%d 个成绩' %len(score1))
print ('%d 成绩最高' % max(score1))
print ('%d 成绩最低' %min(score1))
