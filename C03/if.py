##print("请选择你目前的开发工作:")
##print("1.Windows桌面应用程序")
##print("2.Web应用程序")
##print("3.Web服务")
##
###读取用户的输入字符
##num1=int(input("请输入你的选择:"))
##
###判断用户的输入
##if num1==1:  
##   print("你目前的开发工作是:1.Windows桌面应用程序")
##elif num1 == 2:
##    print("你目前的开发工作是:2.Web应用程序");
##elif  num1== 3:
##    print("你目前的开发工作是:3.Web服务");
##else:
##    print("对不起你选择错误,下次请输入1-3之间的整数");
##

#判断闰年
num1=int(input("请输入一个年份："))
if num1%100 ==0:
    if num1%400==0:
        print("是闰年")
    else:
        print("不是闰年")
else:
    if num1%4==0:
        if num1%100 !=0:
            print("是闰年")
    else:
        print("不是闰年")

    
