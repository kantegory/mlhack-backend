from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///mlhack.db")
session = sessionmaker(bind=engine)


class Teams(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    case = Column(String)
    solution = Column(String)
    captain_name = Column(String)
    captain_about = Column(String)
    captain_email = Column(String)
    captain_phone = Column(String)
    member_name1 = Column(String)
    member_about1 = Column(String)
    member_email1 = Column(String)
    member_phone1 = Column(String)
    member_name2 = Column(String)
    member_about2 = Column(String)
    member_email2 = Column(String)
    member_phone2 = Column(String)
    member_name3 = Column(String)
    member_about3 = Column(String)
    member_email3 = Column(String)
    member_phone3 = Column(String)


class Startups(Base):
    __tablename__ = "startups"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    site = Column(String)
    stage = Column(String)
    about = Column(String)
    task_about = Column(String)
    specs = Column(String)
    addition = Column(String)
    presentation = Column(String)
    country = Column(String)
    team_lead = Column(String)
    email = Column(String)
    phone = Column(String)


Base.metadata.create_all(bind=engine)
