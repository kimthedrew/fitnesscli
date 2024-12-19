# import sqlite3

# CONN = sqlite3.connect('company.db')
# CURSOR = CONN.cursor()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///fitness_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()
