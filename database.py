from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:2709@localhost:5432/API_database")


session = sessionmaker(bind=engine,autoflush=False)