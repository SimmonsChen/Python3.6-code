##set1=set([1,200,39,50])
##set2=set(['王晓光','男'])
##print(set1)
##print(set2)
##set1=set('hello')
##print(set1)

##set1=set([1,200,39,50])
##set1.add(30)
##print('1.add 30：',set1)
##
##set2=set1.copy()
##print('2.copy：',set2)
##
##print(id(set1),id(set2))
##set1.discard(200) #删除指定元素，没有不会报错
##print('3.discard：',set1)
##
##set1.pop()
##print('4.pop：',set1)
##
##set1.remove(39) # 删除指定元素，没有会进行报错
##print('5.remove：',set1)
##
##set1.update([300,500])
##print('6.update：',set1)
##
##set1.clear()
##print('7.clear：',set1)

##set1=set([1,200,39,50])
##del set1
##print(set1)

set1=set([1,200,39,50,89])
set2=set([19,200,3,50,39,1])
print(set1)
print(set2)

print('1.issubset：',set1.issubset(set2))# set1.issubset (set2),检查set1 每个元素是否都在set2中
print('1.set1 <= set2：',set1 <= set2)

print('2.issuperset：',set1.issuperset(set2))#检查set2 的每个元素是否在set1 中
print('2.set1>=set2: ',set1>=set2 )
print('3.union：',set1.union(set2)) # 并集
print('4.intersection：',set1.intersection(set2)) # 交集
print('5.difference：',set2.difference(set1))# set2-set1,包含在SET2 但是不包含在SET1中
print('6 difference: ', set1-set2)# 包含在SET1 但是不包含在SET2中
print('7.symmetric_difference：',set1.symmetric_difference(set2))# set1^ set2 , 包含set1和set2 中不重复的元素，对称差集






