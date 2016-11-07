from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_Cincy_boy_declarative import Anime, Base, Meme, Random, Trump

engine = create_engine('sqlite:///sqlalchemy_twitter_bot.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def update(kind, topic, statement):
    new_statement = kind(topics=str(topic), statements=str(statement))
    session.add(new_statement)
    session.commit()

more = 1
while more == 1:
    decide = input("Would you like to enter a new statement?(Yes/No): ")
    if decide == 'Yes':
        more = 1
        print("What type of statement would you like to input")
        kind = input("Anime?\nMeme?\nRandom?\nTrump?\n: ")
        topic = input("What is the topic of your statement?(One word): ")
        statement = input("Please enter your statement as a string: ")
        if kind == "Anime":
            update(Anime, topic, statement)
        elif kind == "Meme":
            update(Meme, topic, statement)
        elif kind == "Random":
            update(Random, topic, statement)
        else:
            update(Trump, topic, statement)


        print("Your statement has been added to our database")
    else:
        more = 0
