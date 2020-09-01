str1 = 'Hello'
str2 = "Python"
str3 = "!"
strjoin1=str1+" "+str2+" "+str3

strq=('Hello','Python','!')
strflag=" "
strjoin2=strflag.join(strq)

strjoin3='%s %s %s' % (str1,str2,str3)

print ("1.+拼接: ", strjoin1)
print ("2.join拼接: ", strjoin2)
print ("3.格式化拼接: ", strjoin3) # 
print ( r"这里介绍\n的使用")
print ( "这里介绍\n的使用")


