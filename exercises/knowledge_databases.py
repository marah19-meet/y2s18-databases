from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article,category,rate):
	article_object=Knowledge(
		article=article,
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


def delete_article_by_topic(name):
	session.query(Knowledge).filter_by(
		name=name).delete()
	session.commit()

#delete_article_by_topic("adi")

def delete_all_articles():
	session.query(Knowledge).all().delete()
	session.commit()
	

def edit_article_rating(article_title,updated_rating):
	article_object=session.query(Knowledge).filter_by(article=article_title).first()
	article_object.rate = updated_rating
	session.commit()




add_article("soccer",'sport',5)
query_all_articles()
#query_article_by_topic('soccer')
# delete_article_by_topic('name')
#delete_all_articles()
#edit_article_rating('soccer',8)
