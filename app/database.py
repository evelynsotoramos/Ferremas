from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

datebase_url= "mysql+pymysql://root:@localhost:3306/db_ferremas"

engine= create_engine(datebase_url)
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base= declarative_base()