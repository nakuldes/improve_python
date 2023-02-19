from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("sn", Integer, primary_key = True)
    firstname = Column("firstname", String)
    gender = Column("gender", CHAR) 
    age = Column('age', Integer)


    def __init__(self, ssn, first, gender, age) -> None:
        self.ssn = ssn
        self.firstname = first
        self.gender = gender
        self.age = age

    def __repr__(self) -> str:
        return f'({self.ssn}) ({self.firstname}) ({self.gender}) ({self.age})'

engine = create_engine("sqlite:///ppl.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(1, 'Mike', 'm', 35)
session.add(person)
session.commit()

#workspace/classes.txt:workspace/input.jpg:workspace/alexnet-pretrained.pt:workspace/result.txt