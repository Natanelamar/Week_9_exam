from fastapi import FastAPI, HTTPException
from db_init import init_database 
from db import get_db_connection
import dal

app = FastAPI()

init_database()

cnx = get_db_connection()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    try: 
        data = dal.get_customers_by_credit_limit_range(cnx)
        return {"res": data}
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/q2/orders-null-comments")
def orders_null_comments():
    try: 
        data = dal.get_orders_with_null_comments(cnx)
        return {"res": data}
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/q3/customers-first-5")
def customers_first_5():
    try: 
        data = dal.get_first_5_customers(cnx)
        return {"res": data}
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/q4/payments-total-average")
def payments_total_average():
    try: 
        data = dal.get_payments_total_and_average(cnx)
        return {"res": data}
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/q5/employees-office-phone")
def employees_office_phone():
    try: 
        data = dal.get_employees_with_office_phone(cnx)
        return {"res": data}
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    try: 
        data = dal.get_customers_with_shipping_dates(cnx)
        return {"res": data}
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    try: 
        data = dal.get_customer_quantity_per_order(cnx)
        return {"res": data}
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern():
    try: 
        data = dal.get_customers_payments_by_lastname_pattern(cnx)
        return {"res": data}
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))