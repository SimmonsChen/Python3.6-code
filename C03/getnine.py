def getnine():
     lis=[]
     for i in range(1,10):
         for j in range(1,i+1):
             lis.append(str(i)+"*"+str(j)+"="+str(i*j))
     return lis

print(getnine())
