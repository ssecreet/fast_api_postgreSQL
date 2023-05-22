from sqlalchemy import Column, Boolean, String, ARRAY, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    spouse_id = Column(Integer, nullable=True)
    kids_ids = Column(ARRAY(Integer))
    is_married = Column(Boolean, nullable=False)
