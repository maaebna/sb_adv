from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///recipes.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    cook_time = Column(Integer)
    ingredients = Column(String(255))
    description = Column(String(255))
    views = Column(Integer, default=0)


Base.metadata.create_all(bind=engine)
