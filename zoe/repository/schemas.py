from typing import Union
from pydantic import BaseModel, root_validator
from .data.calculations_uk import (taxable_yearly_income,
                                   btr_difference, htr_difference, yearly_tax_btr, yearly_tax_htr, yearly_income_tax,
                                   monthly_gross_income, monthly_taxable_income, weekly_gross_income, weekly_personal_allowance,
                                   weekly_taxable_income, weekly_taxable_PT_NI, weekly_taxable_ST_NI, weekly_PT_NI_contribution,
                                   weekly_ST_NI_contribution, total_weekly_NI_contribution, weekly_income_tax, weekly_total_tax,
                                   weekly_net_income, hourly_gross_income, hourly_net_income, total_monthly_NI_contribution,
                                   monthly_income_tax, monthly_total_tax, yearly_pension_contribution, monthly_pension_contribution,
                                   monthly_net_income, yearly_NI_contribution, approx_total_yearly_tax, years_before_retirement,
                                   work_hours_per_year, hours_left_before_retirement, approx_monthly_savings, approx_yearly_savings,
                                   approx_yearly_expenses, total_earned_now_retirement, total_expenses_now_retirement, total_tax_now_retirement,
                                   total_tax_paid, total_cash_left_retirement, total_Cash_left_percent, total_pension_now_retirement,
                                   have_cash_amount_desired_by_retirement, yearly_state_pension_payout, pension_payout_15yrs,
                                   pension_payout_20yrs, pension_payout_30yrs)


class InputFinanceData(BaseModel):
    gross_annual_salary: Union[int, float]
    monthly_expenses: Union[int, float]
    weekly_work_hours: Union[int, float]
    pension: bool
    age: int
    retirement_age: int
    retirement_cash: Union[int, float]
    currency: str


class ResponseInputFinanceData(BaseModel):
    gross_annual_salary: Union[int, float]
    monthly_expenses: Union[int, float]
    weekly_work_hours: Union[int, float]
    pension: bool
    age: int
    retirement_age: int
    retirement_cash: Union[int, float]
    currency: str  # TODO validate currency to ensure its British Pounds
    Taxable_Yearly_Income: Union[int, float] = None
    BTR_Difference: Union[int, float] = None
    HTR_Difference: Union[int, float] = None
    Yearly_Tax_at_BTR: Union[int, float] = None
    Monthly_Gross_Income: Union[int, float] = None
    Yearly_Tax_at_HTR: Union[int, float] = None
    Yearly_Income_Tax: Union[int, float] = None
    Monthly_Taxable_Income: Union[int, float] = None
    Weekly_Gross_Income: Union[int, float] = None
    Weekly_Personal_Allowance: Union[int, float] = None
    Weekly_Taxable_Income: Union[int, float] = None
    Weekly_Taxable_PT_NI: Union[int, float] = None
    Weekly_PT_NI_Contribution: Union[int, float] = None
    Weekly_Taxable_ST_NI: Union[int, float] = None
    Weekly_ST_NI_Contribution: Union[int, float] = None
    Total_weekly_NI_Contribution: Union[int, float] = None
    Weekly_Income_Tax: Union[int, float] = None
    Weekly_Total_Tax: Union[int, float] = None
    Weekly_Net_Income: Union[int, float] = None
    Hourly_Gross_Income: Union[int, float] = None
    Hourly_Net_Income: Union[int, float] = None
    Total_Monthly_NI_Contribution: Union[int, float] = None
    Monthly_Income_Tax: Union[int, float] = None
    Monthly_Total_Tax: Union[int, float] = None
    Yearly_Pension_Contribution: Union[int, float] = None
    Monthly_Pension_Contribution: Union[int, float] = None
    Monthly_Net_Income: Union[int, float] = None
    Yearly_NI_Contribution: Union[int, float] = None
    Approx_Total_Yearly_Tax: Union[int, float] = None
    Years_Before_Retirement: int = None
    Work_Hours_Per_Year: Union[int, float] = None
    Hours_Left_Before_Retirement: int = None
    Approx_Monthly_Savings: Union[int, float] = None
    Approx_Yearly_Savings: Union[int, float] = None
    Approx_Yearly_Expenses: Union[int, float] = None
    Total_Earned_Now_Retirement: Union[int, float] = None
    Total_Expenses_Now_Retirement: Union[int, float] = None
    Total_Tax_Now_Retirement: Union[int, float] = None
    Total_Tax_Paid: Union[int, float] = None
    Total_Cash_Left_Retirement: Union[int, float] = None
    Total_Cash_Left_Percent: Union[int, float] = None
    Total_Pension_Now_Retirement: Union[int, float] = None
    Have_Cash_Amount_Desired_By_Retirement: bool = None
    Yearly_State_Pension_Payout: Union[int, float] = None
    Pension_Payout_15yrs: Union[int, float] = None
    Pension_Payout_20yrs: Union[int, float] = None
    Pension_Payout_30yrs: Union[int, float] = None

    @root_validator(pre=False)
    def calculate_financial_projections(cls, values):
        values["Taxable_Yearly_Income"] = taxable_yearly_income(
            INP1=values["gross_annual_salary"])
        values["BTR_Difference"] = btr_difference()
        values["HTR_Difference"] = htr_difference(
            values["Taxable_Yearly_Income"], values["BTR_Difference"])
        values["Yearly_Tax_at_BTR"] = yearly_tax_btr(
            values["Taxable_Yearly_Income"], values["BTR_Difference"])
        values["Yearly_Tax_at_HTR"] = yearly_tax_htr(values["HTR_Difference"])
        values["Yearly_Income_Tax"] = yearly_income_tax(
            values["Yearly_Tax_at_BTR"], values["Yearly_Tax_at_HTR"])
        values["Monthly_Gross_Income"] = monthly_gross_income(
            INP1=values["gross_annual_salary"])
        values["Monthly_Taxable_Income"] = monthly_taxable_income(
            values["Taxable_Yearly_Income"])
        values["Weekly_Gross_Income"] = weekly_gross_income(
            values["gross_annual_salary"])
        values["Weekly_Personal_Allowance"] = weekly_personal_allowance()
        values["Weekly_Taxable_Income"] = weekly_taxable_income(
            values["Weekly_Gross_Income"], values["Weekly_Personal_Allowance"])
        values["Weekly_Taxable_PT_NI"] = weekly_taxable_PT_NI(
            values["Weekly_Personal_Allowance"], values["Weekly_Taxable_Income"])
        values["Weekly_PT_NI_Contribution"] = weekly_PT_NI_contribution(
            values["Weekly_Taxable_PT_NI"])
        values["Weekly_Taxable_ST_NI"] = weekly_taxable_ST_NI(
            values["Weekly_Taxable_Income"], values["Weekly_Taxable_PT_NI"])
        values["Weekly_ST_NI_Contribution"] = weekly_ST_NI_contribution(
            values["Weekly_Taxable_ST_NI"])
        values["Total_weekly_NI_Contribution"] = total_weekly_NI_contribution(
            values["Weekly_PT_NI_Contribution"], values["Weekly_ST_NI_Contribution"])
        values["Weekly_Income_Tax"] = weekly_income_tax(
            values["Yearly_Income_Tax"])
        values["Weekly_Total_Tax"] = weekly_total_tax(
            values["Weekly_Income_Tax"], values["Total_weekly_NI_Contribution"])
        values["Weekly_Net_Income"] = weekly_net_income(
            values["Weekly_Gross_Income"], values["Weekly_Total_Tax"])
        values["Hourly_Gross_Income"] = hourly_gross_income(
            values["weekly_work_hours"], values["Weekly_Gross_Income"])
        values["Hourly_Net_Income"] = hourly_net_income(
            values["weekly_work_hours"], values["Weekly_Net_Income"])
        values["Total_Monthly_NI_Contribution"] = total_monthly_NI_contribution(
            values["Total_weekly_NI_Contribution"])
        values["Monthly_Income_Tax"] = monthly_income_tax(
            values["Yearly_Income_Tax"])
        values["Monthly_Total_Tax"] = monthly_total_tax(
            values["Total_Monthly_NI_Contribution"], values["Monthly_Income_Tax"])
        values["Yearly_Pension_Contribution"] = yearly_pension_contribution(
            values["gross_annual_salary"], values["pension"])
        values["Monthly_Pension_Contribution"] = monthly_pension_contribution(
            values["pension"], values["Yearly_Pension_Contribution"])
        values["Monthly_Net_Income"] = monthly_net_income(
            values["Monthly_Gross_Income"], values["Monthly_Total_Tax"], values["Monthly_Pension_Contribution"])
        values["Yearly_NI_Contribution"] = yearly_NI_contribution(
            values["Total_Monthly_NI_Contribution"])
        values["Approx_Total_Yearly_Tax"] = approx_total_yearly_tax(
            values["Yearly_Income_Tax"], values["Yearly_NI_Contribution"])
        # --------------------- OUC Section ---------------------------------------------
        values["Years_Before_Retirement"] = years_before_retirement(
            values["age"])
        values["Work_Hours_Per_Year"] = work_hours_per_year(
            values["weekly_work_hours"])
        values["Hours_Left_Before_Retirement"] = hours_left_before_retirement(
            values["Work_Hours_Per_Year"], values["Years_Before_Retirement"])
        values["Approx_Monthly_Savings"] = approx_monthly_savings(
            values["Monthly_Net_Income"], values["monthly_expenses"])
        values["Approx_Yearly_Savings"] = approx_yearly_savings(
            values["Approx_Monthly_Savings"])
        values["Approx_Yearly_Expenses"] = approx_yearly_expenses(
            values["monthly_expenses"])
        values["Total_Earned_Now_Retirement"] = total_earned_now_retirement(
            values["gross_annual_salary"], values["Years_Before_Retirement"])
        values["Total_Expenses_Now_Retirement"] = total_expenses_now_retirement(
            values["Approx_Yearly_Expenses"], values["Years_Before_Retirement"])
        values["Total_Tax_Now_Retirement"] = total_tax_now_retirement(
            values["Approx_Total_Yearly_Tax"], values["Years_Before_Retirement"])
        values["Total_Tax_Paid"] = total_tax_paid(
            values["Total_Tax_Now_Retirement"], values["Total_Earned_Now_Retirement"])
        values["Total_Cash_Left_Retirement"] = total_cash_left_retirement(
            values["Approx_Yearly_Savings"], values["Years_Before_Retirement"])
        values["Total_Cash_Left_Percent"] = total_Cash_left_percent(
            values["Total_Cash_Left_Retirement"], values["Total_Earned_Now_Retirement"])
        values["Total_Pension_Now_Retirement"] = total_pension_now_retirement(
            values["pension"], values["Yearly_Pension_Contribution"], values["Years_Before_Retirement"])
        values["Have_Cash_Amount_Desired_By_Retirement"] = have_cash_amount_desired_by_retirement(
            values["Total_Cash_Left_Retirement"], values["retirement_cash"])
        values["Yearly_State_Pension_Payout"] = yearly_state_pension_payout()
        values["Pension_Payout_15yrs"] = pension_payout_15yrs(
            values["Yearly_State_Pension_Payout"])
        values["Pension_Payout_20yrs"] = pension_payout_20yrs(
            values["Yearly_State_Pension_Payout"])
        values["Pension_Payout_30yrs"] = pension_payout_30yrs(
            values["Yearly_State_Pension_Payout"])

        return values


# class NewUser(BaseModel):
#     name: str
#     user_id: str = uuid.uuid4()
#     email: str
#     password: str
#     country: str


# class ShowNewUser(BaseModel):
#     name: str
#     email: str
#     country: str

#     class Config:
#         orm_mode = True

# test = InputFinanceData(gross_annual_salary=50000, monthly_expenses=4000, weekly_work_hours=40,
#                         pension=True, age=22, retirement_age=26, retirement_cash=58, currency='USD')
# print(test)
