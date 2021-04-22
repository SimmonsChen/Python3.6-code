### Chapter1 基础语法

#### 1. 编码

默认情况下，Python 3 源码文件以 **UTF-8** 编码，所有字符串都是 unicode 字符串。

```python
# -*- coding: cp-1252 -*- # 指定不同的编码
```

#### 2. 保留字

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

#### 3. 行与缩进

python最具特色的就是使用缩进来表示代码块，不需要使用大括号 **{}** 。

**缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。**

#### 4. import 与from … import 

在 python 用 **import** 或者 **from...import** 来导入相应的模块。

将整个模块(somemodule)导入，格式为： **import somemodule**

从某个模块中导入某个函数,格式为： **from somemodule import somefunction**

从某个模块中导入多个函数,格式为： **from somemodule import firstfunc, secondfunc, thirdfunc**

将某个模块中的全部函数导入，格式为： **from somemodule import \***

#### 5. 命令行参数

Python可以使用-h参数查看各参数帮助信息

