"""
This script creates the financial figures from user input - For UK only
"""

YEARLY_PERSONAL_ALLOWANCE = 12570  # CON1
BASIC_INCOME_TAX_RATE = 20  # % PERCENT - CON2
BTR_THRESHOLD = 50270  # CON3
HIGHER_INCOME_TAX_RATE = 40  # % PERCENT - CON4
GOVT_RETIREMENT_AGE = 68  # CON5
EARLIEST_PENSION_RETIREMENT_AGE = 55  # CON6
YEARLY_WEEKS = 52  # CON7
AVG_WORK_WEEKS_PER_YEAR = 49  # CON8
YEARLY_PENSION_ALLOWANCE = 6240  # CON9
PENSION_CONTRIBUTION = 5  # % PERCENT - CON10
NI_PRIMARY_THRESHOLD = 967  # CON11
NI_CONTRIBUTION_FOR_PT = 13.25  # % PERCENT - CON12
NI_CONTRIBUTION_FOR_SECONDARY_THRESHOLD = 3.25  # % PERCENT - CON13
LIFE_EXPECTANCY_AGE = 88  # CON14
WEEKLY_STATE_PENSION_PAYOUT = 181.15  # CON15
MINIMUM_INCOME_ESSENTIAL_LIFESTYLE = 13000  # CON16

# -----------------------------INCOME CALCULATIONS -------------------------------------
# TODO: add docstrings to functions


def taxable_yearly_income(INP1, CON1=YEARLY_PERSONAL_ALLOWANCE):  # INC1
    return INP1 - CON1


def btr_difference(CON3=BTR_THRESHOLD,  CON1=YEARLY_PERSONAL_ALLOWANCE):  # INC2
    return CON3 - CON1


def htr_difference(INC1, INC2):  # INC3
    """
    Args:

    INC1 = taxable_yearly_income
    INC2 = btr_difference
    """
    if INC1 > INC2:
        return INC1 - INC2
    else:
        return 0


def yearly_tax_btr(INC1, INC2, CON2=BASIC_INCOME_TAX_RATE, CON3=BTR_THRESHOLD):  # INC4
    """
    Args:
    INC1 = taxable_yearly_income
    INC2 = btr_difference
    """
    if INC1 > CON3:
        return INC2 * (CON2/100)
    else:
        return INC1 * (CON2/100)


def yearly_tax_htr(INC3, CON4=HIGHER_INCOME_TAX_RATE):  # INC5
    """
    Args:
    INC3 = htr_difference
    """
    return INC3 * (CON4/100)


def yearly_income_tax(INC4, INC5):  # INC6
    """
    Args:
    INC4 = yearly_tax_btr
    INC5 = yearly_tax_htr
    """
    return INC4 + INC5


def monthly_gross_income(INP1):  # INC7
    return round(INP1/12, 2)


def monthly_taxable_income(INC1):  # INC8
    """
    Args:
    INC1 = taxable_yearly_income
    """
    return round(INC1/12, 2)


def weekly_gross_income(INP1, CON7=YEARLY_WEEKS):  # INC9
    return round(INP1/CON7, 2)


def weekly_personal_allowance(CON1=YEARLY_PERSONAL_ALLOWANCE, CON7=YEARLY_WEEKS):  # INC10
    return round(CON1/CON7, 2)


def weekly_taxable_income(INC9, INC10):  # INC11
    """
    Args:
    INC9 = weekly_gross_income
    INC10 = weekly_personal_allowance
    """
    return INC9 - INC10


def weekly_taxable_PT_NI(INC10, INC11, CON11=NI_PRIMARY_THRESHOLD):  # INC12
    """
    Args:
    INC10 = weekly_personal_allowance
    INC11 = weekly_taxable_income
    """
    if CON11 - INC10 >= INC11:
        return INC11
    else:
        return round(CON11 - INC10, 2)


def weekly_PT_NI_contribution(INC12, CON12=NI_CONTRIBUTION_FOR_PT):  # INC13
    """
    Args:
    INC12=weekly_taxable_PT_NI
    """
    return round(INC12 * (CON12/100), 2)


def weekly_taxable_ST_NI(INC11, INC12):  # INC14
    """
    Args:
    INC11 = weekly_taxable_income, 
    INC12 = weekly_taxable_PT_NI

    """
    if INC11 - INC12 > 0:
        return INC11 - INC12
    else:
        return 0


def weekly_ST_NI_contribution(INC14, CON13=NI_CONTRIBUTION_FOR_SECONDARY_THRESHOLD):  # INC15
    """
    Args:
    INC14 = weekly_taxable_ST_NI
    """
    return round(INC14 * (CON13/100), 2)


def total_weekly_NI_contribution(INC13, INC15):  # INC16
    """
    Args:
    INC13 = weekly_PT_NI_contribution, 
    INC15 = weekly_ST_NI_contribution
    """
    return INC13 + INC15


def weekly_income_tax(INC6, CON7=YEARLY_WEEKS):  # INC17
    """
    Args:
    INC6 = yearly_income_tax
    """
    return round(INC6/CON7, 2)


def weekly_total_tax(INC17, INC16):  # INC18
    """
    Args:
    INC17 = weekly_income_tax
    INC16 = total_weekly_NI_contribution
    """
    return INC17 + INC16


def weekly_net_income(INC9, INC18):  # INC19
    """
    Args:
    INC9 = weekly_gross_income
    INC18 = weekly_total_tax
    """
    return INC9 - INC18


def hourly_gross_income(INP3, INC9):  # INC20
    """
    Args:
    INC9 = weekly_gross_income
    INP3 = weekly_work_hours
    """
    return round(INC9/INP3, 2)


def hourly_net_income(INP3, INC19):  # INC21
    """
    INP3 = weekly_work_hours
    INC19 = weekly_net_income
    """
    return round(INC19/INP3, 2)


def total_monthly_NI_contribution(INC16):
    """
    Args:
    INC16 = total_weekly_NI_contributio
    """
    return round(INC16 * 4.33, 2)


def monthly_income_tax(INC6):  # INC23
    """
    Args:
    INC6 = yearly_income_tax
    """
    return round(INC6/12, 2)


def monthly_total_tax(INC22, INC23):  # INC24
    """
    Args:
    INC22 = total_monthly_NI_contribution
    INC23 = monthly_income_tax
    """
    return INC22 + INC23


def yearly_pension_contribution(INP1, INP4, CON9=YEARLY_PENSION_ALLOWANCE, CON10=PENSION_CONTRIBUTION):  # INC27 **
    """
    Args:
    INP1 = gross_annual_salary
    INP4 = pension (True/False)
    """
    if INP4:
        return round((INP1 - CON9) * (CON10/100), 2)
    else:
        return 0


def monthly_pension_contribution(INP4, INC27):  # INC25
    """
    Args:
    INP4 = pension (True/False)
    INC27 = yearly_pension_contributio
    """
    if INP4:
        return round(INC27/12, 2)
    else:
        return 0


def monthly_net_income(INC7, INC24, INC25):   # INC26
    """
    Args:
    INC7 = monthly_gross_income
    INC24 = monthly_total_tax
    INC25 = monthly_pension_contribution
    """
    return round(INC7 - INC24 - INC25, 2)


def yearly_NI_contribution(INC22):  # INC28
    """
    Args:
    INC22 = total_monthly_NI_contribution
    """
    return round(INC22 * 12, 2)


def approx_total_yearly_tax(INC6, INC28):  # INC29
    """
    Args:
    INC6 = yearly_income_tax
    INC28 = yearly_NI_contribution
    """
    return INC6 + INC28


# -------------------------------------- OUTPUT CALCULATIONS -----------------------------------------

def years_before_retirement(INP5, CON5=GOVT_RETIREMENT_AGE):   # OUC1
    """
    Args:
    INP5 = user age
    CON5 = GOVT_RETIREMENT_AGE
    """
    return CON5 - INP5


def work_hours_per_year(INP3, CON8=AVG_WORK_WEEKS_PER_YEAR):   # OUC2
    """
    Args:
    INP3 = weekly_work_hours
    CON8 = AVG_WORK_WEEKS_PER_YEAR
    """
    return CON8 * INP3


def hours_left_before_retirement(OUC2, OUC1):   # OUC3
    """
    Args:
    OUC2 = work_hours_per_year
    OUC1 = years_before_retirement
    """

    return OUC2 * OUC1


def approx_monthly_savings(INC26, INP2):  # OUC4
    """
    Args:
    INC26 = monthly_net_income
    INP2 = monthly_expenses
    """

    return round(INC26 - INP2, 2)


def approx_yearly_savings(OUC4):   # OUC5
    """
    Args:
    OUC4 = approx_monthly_savings
    """
    return OUC4 * 12


def approx_yearly_expenses(INP2):   # OUC6
    """
    Args:
    INP2 = monthly_expenses
    """

    return INP2 * 12


def total_earned_now_retirement(INP1, OUC1):  # OUC7
    # TODO: maybe add a yearly cost of living increase based on a %
    """
    Args:
    INP1 = gross_annual_salary
    OUC1 = years_before_retirement
    (Assuming no increment in salary)
    """
    return INP1 * OUC1


def total_expenses_now_retirement(OUC6, OUC1):  # OUC8
    """
    Args:
    OUC6 = approx_yearly_expenses
    OUC1 = years_before_retirement
    """
    return OUC6 * OUC1


def total_tax_now_retirement(INC29, OUC1):  # OUC9
    """
    Args:
    INC29 = approx_total_yearly_tax
    OUC1 = years_before_retirement
    """
    return round(INC29 * OUC1, 2)


def total_tax_paid(OUC9, OUC7):  # OUC10
    """
    Args:
    OUC9 = total_tax_now_retirement
    OUC7 = total_earned_now_retirement
    """
    return round((OUC9/OUC7) * 100, 2)


def total_cash_left_retirement(OUC5, OUC1):  # OUC11
    """
    OUC5 = approx_yearly_savings
    OUC1 = years_before_retirement
    """
    return round(OUC5 * OUC1, 2)


def total_Cash_left_percent(OUC11, OUC7):  # OUC12
    """
    Args:
    OUC11 = total_cash_left_retirement
    OUC7 = total_earned_now_retirement
    """

    return round((OUC11/OUC7) * 100, 2)


def total_pension_now_retirement(INP4, INC27, OUC1):   # OUC13
    """
    Args:
    INP4 = pension (True/False)
    INC27 = yearly_pension_contribution
    OUC1 = years_before_retirement
    """
    if INP4:
        return INC27 * OUC1
    else:
        return 0


def have_cash_amount_desired_by_retirement(OUC11, INP7):  # OUC14
    """
    Args:
    OUC11 = total_cash_left_retirement
    INP7 = retirement_cash
    """
    if OUC11 - INP7 > 0:
        return True
    else:
        return False


def yearly_state_pension_payout(CON15=WEEKLY_STATE_PENSION_PAYOUT):  # OUC15
    return round(CON15 * 52, 2)


def pension_payout_15yrs(OUC15):   # OUC16
    """
    Args:
    OUC15 = yearly_state_pension_payout
    """
    return round(OUC15 * 15, 2)


def pension_payout_20yrs(OUC15):   # OUC17
    """
    Args:
    OUC15 = yearly_state_pension_payout
    """
    return round(OUC15 * 20, 2)


def pension_payout_30yrs(OUC15):   # OUC18
    """
    Args:
    OUC15 = yearly_state_pension_payout
    """
    return round(OUC15 * 30, 2)
