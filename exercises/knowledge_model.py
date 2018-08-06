from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="classmates"
	name=Column(String,primary_key=True)
	article=Column(String)
	category=Column(String)
	rate=Column(Integer)

	###############repr

	def __repr__(self):
		return(("knowledge name:{}\n"
				"knowledge article:{}\n"
			   "knowledge category:{}\n"
			   "knowledge rate:{}\n").format(
			   self.name,self.article,self.category,self.rate))
x=Knowledge(name="adi",article="soccer",category="soccer",rate=5)
print(x)


	

