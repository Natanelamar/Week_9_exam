from fastapi import FastAPI, HTTPException
from db_init import init_database
import dal

app = FastAPI()

init_database()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    try:
        result = dal.get_customers_by_credit_limit_range()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@app.get("/q2/orders-null-comments")
def orders_null_comments():
    try:
        result = dal.get_orders_with_null_comments()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@app.get("/q3/customers-first-5")
def customers_first_5():
    try:
        result = dal.get_first_5_customers()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@app.get("/q4/payments-total-average")
def payments_total_average():
    try:
        result = dal.get_payments_total_and_average()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@app.get("/q5/employees-office-phone")
def employees_office_phone():
    try:
        result = dal.get_employees_with_office_phone()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    try:
        result = dal.get_customers_with_shipping_dates()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    try:
        result = dal.get_customer_quantity_per_order()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern():
    try:
        result = dal.get_customers_payments_by_lastname_pattern()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result
