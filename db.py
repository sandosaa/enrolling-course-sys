from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

data_base_url = "sqlite:///database.db"
engine = create_engine(data_base_url)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()