from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(category,rate):
	article_object=Knowledge(
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
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass

add_article('category','rate')
query_all_articles()
query_article_by_topic('soccer')