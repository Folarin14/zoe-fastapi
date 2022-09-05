# from sqlalchemy import Column, Integer, String, Float, ForeignKey, BOOLEAN
# from sqlalchemy.orm import relationship
# from .database import Base


# class FinanceTable(Base):
#     __tablename__ = 'finance'
#     id = Column(Integer, primary_key=True)
#     gross_annual_salary = Column(Float)
#     currency = Column(String)
#     monthly_expenses = Column(Float)
#     weekly_work_hours = Column(Float)
#     pension = Column(BOOLEAN, unique=False, default=True)
#     age = Column(Integer)
#     retirement_age = Column(Integer)
#     retirement_cash = Column(Float)

#users = relationship("Users", back_populates='finance')


# class Users(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(String, unique=True)
#     name = Column(String)
#     email = Column(String, unique=True)
#     password = Column(String)
#     country = Column(String)

#     finance = relationship(
#         "FinanceTable", back_populates='users', uselist=False)
