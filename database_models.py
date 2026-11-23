
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    price = Column(Float)
    name = Column(String)
    quantity = Column(Integer)
