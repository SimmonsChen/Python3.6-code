##import time
##
##if time.gmtime().tm_year == 2018:
##   for i in range(1,12):
##       print(str(time.gmtime().tm_year) +'年'+str(i)+'月好')
##

##
##from time import *
##
##if gmtime().tm_year == 2018:
##   for i in range(1,12):
##       print(str(gmtime().tm_year) +'年'+str(i)+'月好')
##


import testpackage.testfun

print(testpackage.testfun.square(5))					#25
