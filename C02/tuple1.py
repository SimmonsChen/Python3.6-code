stu1='10001','张晓光','男',20,20
##stu2='10001','张晓光','男',20,20
print(type(stu1))
print('20出现的次数',stu1.count(20))
print('20出现的位置',stu1.index(20))

print('后三项出现的位置',stu1.index(20,3,4))

##del stu1
##print(stu1)

score1=(80,100,98,59)
print('%d个成绩'%len(score1))
print('成绩最高：',max(score1))
print('成绩最低：',min(score1))

stu1=('101','张晓光')
stu2=('男',20)

print('stu1+stu1:',stu1+stu2)
print('stu1*2:',stu1*2)
print('101 in stu1:','101' in stu1)


##列表转元组
stu1=['10001','张晓光','男',20]
tup1=tuple(stu1)  #转元组
print(type(stu1))
print(type(tup1))

##元组转列表
stu1=('10001','张晓光','男',20)
list1=list(stu1)  #转列表
print(type(stu1))
print(type(list1))

