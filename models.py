from sqlalchemy import Column, Integer, String,Boolean
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role=Column(String, nullable=False)
    is_verified= Column(Boolean, default=False)


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mobile_number = Column(String, unique=True, index=True, nullable=False)
    adhar=Column(String, unique=True, index=True, nullable=False)
    working_time=Column(String, nullable=False)
    working_days=Column(String, nullable=False)
    salary=Column(Integer, nullable=False)
