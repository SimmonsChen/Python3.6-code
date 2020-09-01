import threading 
import time

products = []
condition = threading.BarrierCondition()

class Consumer(threading.Thread):
    def consume(self):
        global condition
        global products

        condition.acquire()
        if len(products) == 0:
            condition.wait()
            print ("消费者提醒: 没有产品去消费了")
        products.pop()
        print("消费者提醒: 消费1个产品")
        print("消费者提醒: 还能消费的产品数为"\
              + str(len(products)))
        condition.notify()
        condition.release()
    def run(self):
        for i in range(0, 20):
            time.sleep(4)
            self.consume()

class Producer(threading.Thread):
    def produce(self):
        global condition
        global products

        condition.acquire()
        if len(products) == 10:
            condition.wait()
            print ("生产者提醒: 生产的产品数为"\
                   + str(len(products)))
            print("生产者提醒: 停止生产！")
        products.append(1)
        print("生产者提醒:产品总数为"\
              + str(len(products)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(1)
            self.produce()

producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()
producer.join()
consumer.join()
