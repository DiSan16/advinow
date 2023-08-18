from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()



class Business(Base):
    __tablename__ = "business"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Symptom(Base):
    __tablename__ = "symptoms"

    business_id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String)
    code = Column(String, primary_key=True, index=True)
    name = Column(String)
    diagnostic = Column(String)

    