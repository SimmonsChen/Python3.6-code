##stu1=['10001','张晓光','男',20]
##stu1=[]
##stu1.append('张晓光')
##
##
##
##print('学生学号：%s，学生年龄%d'%(stu1[0],stu1[-1]))
##stu1=['10001','张晓光','男',20]
##print('学生：',stu1[1:3])
##
##
##stu1=[0]*4
##print('学生：',stu1)
##
##stu1[0]='10001'
##stu1[1]='张晓光'
##stu1[2]='男'
##stu1[3]=20
##print('学生：',stu1)

stu1 = [[0]*3 for i in range(3)]
print('学生：',stu1)
stu1[1][3]=25;
print('学生：',stu1[1][3])


##stu1=[[0]*3]*4
##stu1[0][2]='10001'
##print('学生：',stu1)

##stu1=[[0]*3 for i in range(4)]
##stu1 [1][1]="10001"
##print('学生：', stu1)


##stu1=['10001','张晓光','男',20];
##print('学生：',stu1)
##
###1.追加城市
##stu1.append('上海')
##print('1.',stu1)
##
###2.追加另一个列表
##stu2=['10002','李淑霞','女',21,'上海']
##stu1.extend(stu2)
##print('2.',stu1)
##
###3.上海在列表中出现的次数
##print('3.',stu1.count('上海'))
##
###4.获取位置
##print('4.',stu1.index('李淑霞'))
##
###5.插入开头
##stu1.insert(0,'学生信息：')
##print('5.',stu1)
##
###6.pop移除
##stu1.pop(0)
###stu1.pop()
###stu1.pop(-1)
##print('6.',stu1)
##
###7.remove移除
##stu1.remove('上海')
##print('7.',stu1)
##
###8.reverse反转
##stu1.reverse()
##print('8.',stu1)
##
###9.sort排序
##stu1.sort()
##print('9.',stu1)


##stu1=[
##    ['10001','张晓光','男',20],
##    ['10002','李淑霞','女',21],
##    ['10003','王心智','男',19]
##]
##print('学生：',stu1)
