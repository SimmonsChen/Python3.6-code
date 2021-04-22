### Chapter5 函数

定义一个由自己想要功能的函数，以下是简单的规则：

- 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号 **()**。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- **return [表达式]** 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

#### 1. 语法

Python 定义函数使用 def 关键字，一般格式如下：

```python
def 函数名（参数列表）:
    函数体
def hello():
    print("Hello World!")
# 计算面积函数
def area(width, height):
    return width * height 
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
```

#### 2. 函数调用

定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。

这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。

如下实例调用了 **printme()** 函数：

```
# 定义函数
def printme( str ):
   # 打印任何传入的字符串
   print (str)
   return
 
# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
```

#### 3. 参数传递

在 python 中，类型属于对象，变量是没有类型的：

```python
a=[1,2,3]
a="Runoob"
# [1,2,3]是List 类型，"Runobo "是string 类型，变量a 没有类型
```

#### 4. 可更改(mutable)与不可更改(immutable)对象

在 python 中，**strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。**

- **不可变类型：**变量赋值 **a=5** 后再赋值 **a=10**，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
- **可变类型：**变量赋值 **la=[1,2,3,4]** 后再赋值 **la[2]=5** 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

- **不可变类型：**类似 C++ 的值传递，如 整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a)）内部修改 a 的值，则是新生成来一个 a。
- **可变类型：**类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

```python
# python 传不可变对象实例
def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a=1
print(id(a))
change(a)
# 看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id
```

可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：

```python
# 传可变对象实例
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)
>>> 
函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
```

#### 6. 参数

- 必需参数： 

  必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

- 关键字参数

  关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

  使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

- 默认参数

- 不定长参数

  可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：

  ```python
  def functionname([formal_args,] *var_args_tuple ):
     "函数_文档字符串"
     function_suite
     return [expression]
  ```

  加了星号 ***** 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

  ```python
  # 可写函数说明
  def printinfo( arg1, *vartuple ):
     "打印任何传入的参数"
     print ("输出: ")
     print (arg1)
     print (vartuple)
   
  # 调用printinfo 函数
  printinfo( 70, 60, 50 )
  ```

#### 	7. 匿名函数

​	python 使用 lambda 来创建匿名函数。所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

- lambda 只是一个表达式，函数体比 def 简单很多。

- lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。

- lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。

- 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

  ```python
  lambda [arg1 [,arg2,.....argn]]:expression
  # 可写函数说明
  sum = lambda arg1, arg2: arg1 + arg2
   
  # 调用sum函数
  print ("相加后的值为 : ", sum( 10, 20 ))
  print ("相加后的值为 : ", sum( 20, 20 ))
  ```

#### 8. return 函数

**return [表达式]** 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，以下实例演示了 return 语句的用法：

```python
# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
 
# 调用sum函数
total = sum( 10, 20 )
print ("函数外 : ", total)
```

#### 9. 强制位置参数

Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。

在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:

```python
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```

