from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_Cincy_boy_declarative import Anime, Base, Meme, Random, Trump

engine = create_engine('sqlite:///sqlalchemy_twitter_bot.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

new_statement1 = Trump(topics='Cake', statements='I love cake')
session.add(new_statement1)
session.commit()

new_statement2 = Anime(topics='Anime', statements='I don''t know anything about anime')
session.add(new_statement2)
session.commit()

new_statement3 = Random(topics='Random', statements='I like ducks')
session.add(new_statement3)
session.commit()

new_statement4 = Meme(topics='Harambe', statements='R.I.P. Harambe')
session.add(new_statement4)
session.commit()


#from sqlalchemy_Cincy_boy_declarative import Anime, Base, Meme, Random, Trump
#from sqlalchemy import create_engine
#engine = create_engine('sqlite:///sqlalchemy_twitter_bot.db')
#Base.metadata.bind = engine
#from sqlalchemy.orm import sessionmaker
#DBSession = sessionmaker()
#DBSession.bind = engine
#session = DBSession()
#
#session.query(Any_class).all()        to find the first
#variable = session.query(Any_class).filter(Any_class.attribute==value).()
#variable.Any_asset_of_the_class
