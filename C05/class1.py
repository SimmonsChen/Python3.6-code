##
##class testClass:
##    name='张晓晓'
##    def welcome(self):
##        print('欢迎你')
##        print('实例', self)
##        print('类 ', self.__class__)
##w=testClass()
##print(w.name)
##w.welcome()
##    
##
##class MarketMember:
##    def __init__(self):
##        print('欢迎光临')
##    def __del__(self):
##        pass
##m=MarketMember()




##class MarketMember:
##    __count=0
##    __name=''
##    def __init__(self,name,count,age):
##        self.__count += count
##        self.__name =name
##        self.age=age
##    def seek(self):
##        print(self.__name+'年龄'+str(self.age)+'积分为'+str(self.__count))
##
##            
##m=MarketMember('王晓',300,20)
##m.seek()
####m.__count
####m.__name
##m.age
##
##class MarketMember:
##    __name=''
##    count=600
##    def __init__(self,name):
##        self.__name=name
##        print( self.__name+'当前积分为'+str(self.count))
##    def change(self,count1):
##        self.count=self.count+count1
##        print(self.__name+'更改后积分为'+str(self.count))
##
##class MyMember(MarketMember):   # 定义了子类 Mymembe()
##    age=0
##    def seekAge(self):
##        print('年龄为'+str(self.age)+" 积分为"+str(self.count)) # self.count为父类的公开属性
##    
##
##            
##m=MyMember('王晓')
##m.change(500)
####m.age=25
##m.seekAge()
##print (m.count)


##class MarketMember:
##    def __change(self,count):
##        print('更改后积分为'+str(count))
##            
##m=MarketMember()
##m.__change(500)



##class Animals:
##    color=''
##    weight=0
##    def jump(self):
##        print('我能跳')
##
##class Cats:
##    def miaomiao(self):
##        print('喵喵')
##
##class WhiteCat(Animals,Cats):
##    def miaomiao(self):
##        print('白喵喵')
##    def catch(self):
##        print('我才能抓到老鼠')
##
##
##c=WhiteCat()
##c.jump()
##c.miaomiao()
##c.catch()
##    
    


##class Person:
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age
## 
##    def __call__(self,*args):
##        return args[0]+args[1] 
## 
####def add(args):
####    return args[0] + args[1]
##  
##p = Person('王晓光', 20)
##print(p(30,20))


##class Person:
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age
##        self._registry = {
##            'name': name,
##            'age': age
##        }
##    def __getitem__(self, key):
##        if key not in self._registry.keys():
##            raise Exception('Please registry the key:%s first !' % (key,))
##        return self._registry[key]
##    def __setitem__(self, key,value):
##        if key not in self._registry.keys():
##            raise Exception('Please registry the key:%s first !' % (key,))
##        self._registry[key]=value
## 
##p = Person('王晓光', 20)
##print(p['name'],p['age'])
##p['age']=30
##print(p['name'],p['age'])




##class Person:
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##    def __getattribute__(self,item):
##        return super(Person, self).__getattribute__(item)
##    def __setattr__(self,item,value):
##        super(Person, self).__setattr__(item,value)
##    def __delattr__(self,item):
##        print('属性被删除了！' )
##
## 
##p = Person('王晓光', 20)
##print(p.name)
##p.addr='上海'
##print(p.addr)
##del p.addr


##class Descriptor:
##    def __init__(self):
##        self.des = None
## 
##    def __get__(self, instance, owner):
##        return instance.__dict__.get(self.des,None)
## 
##    def __set__(self, instance, value):
##        instance.__dict__[self.des] = value
## 
## 
##class Person:
##    des = Descriptor() #这里的Descriptor就是一个描述符类
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age
##        
##p = Person('王晓光', 20)
##p.des = 100    #这里会调用Descriptor的__set__方法
##print(p.des)   #这里会调用Descriptor的__get__方法

##class Meter:
##    def __init__(self, value=0.0):
##        self.value = float(value)
##    def __get__(self, instance, owner):
##        return self.value
##    def __set__(self, instance, value):
##        self.value = float(value)
##
##class Foot:
##    def __get__(self, instance, owner):
##        return instance.meter * 3.2808
##    def __set__(self, instance, value):
##        instance.meter = float(value) / 3.2808
##
##class Distance:
##    meter = Meter()
##    foot = Foot()
##
##d = Distance()
##print(d.meter, d.foot)  # 0.0, 0.0
##d.meter = 1
##print(d.meter, d.foot)  # 1.0 3.2808
##d.meter = 2
##print(d.meter, d.foot)  # 2.0 6.5616


