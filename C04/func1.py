##def sum1(a,b):
##    "求和函数"
##    s=a+b
##    return s
##a,b=3,20
##print("a+b=",sum1(a,b))

##
##def fun1():
##    print("fun1")
##
##def fun2():
##    fun1()
##    print("fun2")
##
##fun2()

##
##def sum1(a,b=100):
##    "求和函数"
##    s=a+b
##    return s
##x,y=3,20
##print("x+y=",sum1(x,y))

##def store():
##    pass
##print(store())


##def store(food):
##    if food=='bread':
##        return 10
##    if food=='cheese':
##        return 20
##    else:
##        return 0
## 
##print("您选择的价格是",store('cheese'))



##def sum1(a,b):
##    s=a+b
##    return s
##x=3
##print("x+y=",sum1(x))


##def store(food,price):
##    if food=='bread':
##        return price*0.8
##    if food=='cheese':
##        return price*0.5
##    else:
##        return 0
##
##str1=store(price=20,foodd='cheese')
##print("您选择的折后价格是",str1)


##def myprint(x,*y):
##    for i in y:
##        print(i,end=" ")
##    print(x,end=" ")
##
##myprint('end',30,40,50)



###赋值
##x=0	
##
###自定义printer函数
##def printer():
##    print(x)
##    x=1
##    print(x)
##
##printer()
##print(x)




##
##sum1=(lambda x,y:x+y)(1,2)
##print("x+y=",sum1)			


###赋值
##x=0	
##print(x)
###自定义printer函数
##def printer():
##    global x
##    x=1
##    #修改
##    print(x)
##
##printer()
##print(x)

def sum1(a=100,b):
    "求和函数"
    s=a+b
    return s
x=20
print("x的和",sum1(x))


