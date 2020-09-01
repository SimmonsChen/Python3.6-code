i=0
while i<5:
    i+=1
    if i == 3:
        print("i=",i)
        continue
    if i == 4:
        print("i=",i)
else:
    print("i越界了：",i)
print("OVER")
# continue 的错误用法#
##i=0
##while i<5:
##    if i == 3:
##        print("i=",i)
##        continue # 结束本次循环，继续下次循环
##    if i == 4:
##        print("i=",i)
##        i+=1
##else:
##    print("i越界了：",i)
##print("OVER")
