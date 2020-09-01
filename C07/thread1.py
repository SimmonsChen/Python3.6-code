##import threading
##
##def test(x,y):
##    for i in range(x,y):  
##        print(i)  
##  
##thread1 = threading.Thread(name='t1',target=test,args=(1,10))     
##thread2 = threading.Thread(name='t2',target=test,args=(20,26)) 
##thread1.start()  
##thread2.start()  


import threading  
  
class mythread(threading.Thread):  
    def run(self):  
        for i in range(1,10):  
            print(i)  
  
thread1 = mythread();  
thread2 = mythread();  
thread1.start()  
thread2.start()  
