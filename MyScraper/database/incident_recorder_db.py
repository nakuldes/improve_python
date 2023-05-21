from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = "incidents"

    ssn = Column("sn", Integer, primary_key = True)
    servername = Column("servername", String)
    status = Column("status", CHAR) 
    date_time = Column('date_time', Integer)


    def inc(self, ssn, svr, status, time_date):
        self.ssn = ssn
        self.srvname = svr
        self.status = status
        self.time_date = time_date

    def __repr__(self) -> str:
        return f'({self.ssn}) ({self.srvname}) ({self.status}) ({self.time_date})'
    



    

