


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b 				# 注意yield
        a, b = b, a + b 			# 赋值
        n += 1
    #当所有数据都生成完成后，没有数据了，会返回这么一个异常：StopIteration: done，这个done是可以自定义的
    return 'done'
fib_generator = fib(20)
print(fib_generator)
print(fib_generator.__next__())
print(fib_generator.__next__())
print(fib_generator.__next__())
print(fib_generator.__next__())
print(fib_generator.__next__())
print(fib_generator.__next__())
print(fib_generator.__next__())

#前面因为已经使用next方法，取过几个数据了，所以这里直接从最后一次取值的地方开始循环
while True:
    try:
        fib_value = fib_generator.__next__()
        print("fib_value: %s" % fib_value)
    except StopIteration as fibs:
        print("Generator return value: %s " % fibs.value)
        break






