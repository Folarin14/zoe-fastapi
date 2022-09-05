from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from ..repository.models import FinanceTable
# , IncomeCalculation
from ..repository.schemas import InputFinanceData, ResponseInputFinanceData
# from ..repository.database import get_db
#db: Session = Depends(get_db)

router = APIRouter(tags=['Finance'], prefix='/data')


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ResponseInputFinanceData)
def create_finance_data(request: InputFinanceData, ):
    return request
    # new_data = FinanceTable(
    #     gross_annual_salary=request.gross_annual_salary,
    #     currency=request.currency,
    #     monthly_expenses=request.monthly_expenses,
    #     weekly_work_hours=request.weekly_work_hours,
    #     pension=request.pension,
    #     age=request.age,
    #     retirement_age=request.retirement_age,
    #     retirement_cash=request.retirement_cash
    # )

    # db.add(new_data)
    # db.commit()
    # db.refresh(new_data)
    # return new_data


# @router.get('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def get_finance_data_by_id(id: int):
#     data = db.query(FinanceTable).filter(FinanceTable.id == id).first()

#     if not data:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
#                             detail=f"Finance Info with requested id: {id} not found")

#     return data
