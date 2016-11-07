import random
from sqlalchemy_Cincy_boy_declarative import Anime, Base, Meme, Random, Trump
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_twitter_bot.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

anime = session.query(Anime).all()
meme = session.query(Meme).all()
random_table = session.query(Random).all()
trump = session.query(Trump).all()

a = len(anime)
m = len(meme)
r = len(random_table)
t = len(trump)

sub = random.randint(1, 4)
if sub == 1:
    n = random.randint(1, a-1)
    print(anime[n].statements)
elif sub == 2:
    n = random.randint(1, m-1)
    print(meme[n].statements)
elif sub ==3:
    n = random.randint(1, r-1)
    print(random_table[n].statements)
else:
    n = random.randint(1, t-1)
    print(trump[n].statements)
