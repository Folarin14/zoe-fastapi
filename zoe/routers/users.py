# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from repository.schemas import NewUser, ShowNewUser, NewFinanceData
# from repository.database import get_db
# from repository.models import Users, FinanceTable
# from typing import List


# router = APIRouter(tags=['Users'])


# @router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowNewUser)
# def create_user_and_finance(finance_data: NewFinanceData, db: Session = Depends(get_db)):
#     new_user = Users(
#         name=user_data.name,
#         user_id=user_data.user_id,
#         email=user_data.email,
#         password=user_data.password,
#         country=user_data.country

#     )

#     new_finance = FinanceTable(
#         # user_id=user_data.user_id,
#         gross_annual_salary=finance_data.gross_annual_salary,
#         currency=finance_data.currency,
#         monthly_expenses=finance_data.monthly_expenses,
#         weekly_work_hours=finance_data.weekly_work_hours,
#         pension=finance_data.pension,
#         age=finance_data.age,
#         retirement_age=finance_data.retirement_age,
#         retirement_cash=finance_data.retirement_cash
#     )

#     # db.add(new_user)
#     db.add(new_finance)
#     db.commit()
#     # db.refresh(new_user)
#     db.refresh(new_finance)
#     return new_finance


# @router.get('/users', status_code=status.HTTP_200_OK, response_model=List[ShowNewUser], response_model_exclude_defaults=True)
# def get_all_users(db: Session = Depends(get_db)):
#     users = db.query(Users).all()

#     if not users:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
#                             detail=f"Requested Resources is not available")

#     return users


# @router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowNewUser)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(Users).filter(Users.id == id).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
#                             detail=f"User with requested id: {id} not found")

#     return user
