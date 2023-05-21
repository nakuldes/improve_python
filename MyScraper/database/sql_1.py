from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, MetaData, Table, select
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
# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# person = Person(1, 'Mike', 'm', 35)
# person1 = Person(2, 'Mike1', 'f', 40)
# person2 = Person(3, 'Mike2', 'm', 50)
# person3 = Person(4, 'Mike3', 'f', 60)
# session.add(person)
# session.add(person1)
# session.add(person2)
# session.add(person3)
# session.commit()

c = engine.connect()
mt = MetaData()
d = Table('people', mt, autoload=True, autoload_with=engine)
q = select([d.columns.firstname]) #.where(d.columns.age >= 55)
res =c.execute(q)

ls = res.fetchall()
print(ls)


