### Chapter 3   条件语句和循环语句

#### 1. 条件控制

Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。

![img](https://www.runoob.com/wp-content/uploads/2013/11/if-condition.jpg)

- if 语句

  ```python
  if condition_1:
      statement_block_1
  elif condition_2:   # elif 替代 else if 
      statement_block_2
  else:
      statement_block_3
  ```

  1. 每个条件后面要使用冒号 **:**，表示接下来是满足条件后要执行的语句块。
  2. 使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
  3. **在Python中没有switch – case语句**

- if 嵌套

  在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。

  ```
  if 表达式1:
      语句
      if 表达式2:
          语句
      elif 表达式3:
          语句
      else:
          语句
  elif 表达式4:
      语句
  else:
      语句
  ```

  ```python
  num=int(input("输入一个数字："))
  if num%2==0:
      if num%3==0:
          print ("你输入的数字可以整除 2 和 3")
      else:
          print ("你输入的数字可以整除 2，但不能整除 3")
  else:
      if num%3==0:
          print ("你输入的数字可以整除 3，但不能整除 2")
      else:
          print  ("你输入的数字不能整除 2 和 3")
  ```

#### 2. 循环语句

##### 2.1  for 循环

Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串

![img](https://www.runoob.com/wp-content/uploads/2013/11/A71EC47E-BC53-4923-8F88-B027937EE2FF.jpg)

```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
# 实例
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```

##### 2.2 while 循环

```
while 判断条件(condition)：
    执行语句(statements)……
```

![img](https://www.runoob.com/wp-content/uploads/2013/11/886A6E10-58F1-4A9B-8640-02DBEFF0EF9A.jpg)

```python
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1 
print("1 到 %d 之和为: %d" % (n,sum))
```

##### 2.3 while 循环使用else 语句

在 while … else 在条件语句为 false 时执行 else 的语句块。**在 Python 中没有 do..while 循环。**

```python
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
# 实例
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
```

##### 2.4 range () 函数

如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列

```python
for i in range(5,9):
	print(i)
# for 结合len
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i])
```

##### 2.5 无限循环

while（1）实现无限循环，crtl+c 退出

##### 2.6 break 和continue 语句及循环中else 子句

![img](https://www.runoob.com/wp-content/uploads/2014/09/E5A591EF-6515-4BCB-AEAA-A97ABEFC5D7D.jpg)

![img](https://www.runoob.com/wp-content/uploads/2014/09/8962A4F1-B78C-4877-B328-903366EA1470.jpg)

**break** 语句可以**跳出 for 和 while 的循环体。**如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

**continue** 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

```python
# while 中使用break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # 此处跳出while 循环
    print(n)
print('循环结束。')
# while 中使用continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')
```

##### 2.7 pass 语句

Python pass是空语句，是为了保持程序结构的完整性。