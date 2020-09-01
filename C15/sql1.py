
##class Student():
##    def __init__(self, id, name,age,address):
##        self.id = id
##        self.name = name
##        self.age = age
##        self.address = address
##
##
##s=Student(1,'刘晓华',16,'北京市海淀区')
##print(s.name)

##
##from sqlalchemy import create_engine
##engine = create_engine("mysql+mysqldb://root:@localhost:3306/Students?charset=utf8")
##print(engine)


from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'#表的名称
    #表的结构
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    age = Column(Integer)
    address = Column(String(30))

engine = create_engine("mysql+mysqldb://root:@localhost:3306/Students?charset=utf8")
Session = sessionmaker(bind=engine)     #创建持久化对象
session = Session()

##s=Student(id=1,name='刘晓华',age =16,address='北京市海淀区')
##session.add(s)
ss = session.query(Student).one()# 返回数据表所有数据
session.commit()
print(ss.name)
session.close()

