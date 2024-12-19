
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.db.session import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    workouts = relationship('WorkoutSession', back_populates='user')

class WorkoutSession(Base):
    __tablename__ = 'workout_sessions'
    id = Column(Integer, primary_key=True)
    workout_type = Column(String)
    duration = Column(Integer)  # duration in minutes
    date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='workouts')
