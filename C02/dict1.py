##stu1={'学号':'10001','姓名':'张晓光','性别':'男','年龄':20}
##stu1['年龄']=30
##print(stu1['性别'])
##print(stu1)

##
##stu1={'学号':'10001','姓名':'张晓光','姓名':'李三','年龄':20}
##print(stu1[1])

##
##day={1:'星期一',2:'星期二',3:30,'四':'星期四'}
##
##print(day['四'])
##print(day[2])
##print(day[3])

##
##dict1={'姓名':'张晓光','年龄':20}
##
##print('1.所有键：',dict1.keys())
##print('2.所有值：',dict1.values())
##print('3.所有键-值：',dict1.items())
##
##dict2=dict1
##dict3=dict1.copy()# 使用Copy 函数进行深拷贝
##print('4.浅拷贝和深拷贝：',id(dict1),id(dict2),id(dict3))
##
##score1=(1,2,3,4)
##dict4=dict1.fromkeys(score1)
##print('%s 字典中所有值；',dict4.values())
##print('%s 字典中所有键；',dict4.keys())
##print('5.通过元组创建字典：',dict4)
##print('6.get年龄：',dict1.get('年龄'))

##dict1.setdefault('年纪',30)
##print('7.setdefault年纪：',dict1)
##
##dict5={'成绩':'优良'}
##dict1.update(dict5)
##print('8.update成绩：',dict1)


##删除字典

dict1={'姓名':'张晓光','年龄':20}
if '姓名' in dict1:
    print(dict1['姓名'])

if '性别' not in dict1:
    dict1.setdefault('性别','男')
    print(dict1)
