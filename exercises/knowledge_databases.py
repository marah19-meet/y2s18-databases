from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,category,rate):
	article_object=Knowledge(
		name=name,
		category=category,
		rate=rate
	)
	session.add(article_object)
	session.commit()
def query_all_articles():
	ques=session.query(
		Knowledge).all()
	return ques
	

def query_article_by_topic(article):
	specific=session.query(Knowledge).filter_by(
		article=article).first()
	return specific
print(query_article_by_topic('soccer'))


def delete_article_by_topic():
	session.query(Knowledge).filter_by(
		nanme=name).delete()
	session.commit()

delete_student("adi")

def delete_all_articles():
	session.query(Knowledge).all().delete()
	session.commit()
	

#def edit_article_rating():
#	pass

add_article('name','category','rate')
query_all_articles()
query_article_by_topic('soccer')