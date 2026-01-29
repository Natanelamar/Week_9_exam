from fastapi import FastAPI
from db_init import init_database
import dal 
import sql_conetion


app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    connection = sql_conetion.Sql_connector()
    connection.cursor.execute(dal.get_customers_by_credit_limit_range())
    info = connection.cursor.fetchall()
    connection.cursor.close()
    return {'data': info}

@app.get("/q2/orders-null-comments")
def orders_null_comments():
    connection = sql_conetion.Sql_connector()
    connection.cursor.execute(dal.get_orders_with_null_comments)
    info = connection.cursor.fetchall()
    connection.cursor.close()
    return {'data': info}

@app.get("/q3/customers-first-5")
def customers_first_5():
    connection = sql_conetion.Sql_connector()
    connection.cursor.execute(dal.get_first_5_customers())
    info = connection.cursor.fetchall()
    connection.cursor.close()
    return {'data': info}

@app.get("/q4/payments-total-average")
def payments_total_average():
    connection = sql_conetion.Sql_connector()
    connection.cursor.execute(dal.get_payments_total_and_average)
    info = connection.cursor.fetchall()
    connection.cursor.close()
    return {'data': info}

@app.get("/q5/employees-office-phone")
def employees_office_phone():
    connection = sql_conetion.Sql_connector()
    connection.cursor.execute(dal.get_employees_with_office_phone())
    info = connection.cursor.fetchall()
    connection.cursor.close()
    return {'data': info}

@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    connection = sql_conetion.Sql_connector()
    connection.cursor.execute(dal.get_customers_with_shipping_dates())
    info = connection.cursor.fetchall()
    connection.cursor.close()
    return {'data': info}

@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    connection = sql_conetion.Sql_connector()
    connection.cursor.execute(dal.get_customer_quantity_per_order())
    info = connection.cursor.fetchall()
    connection.cursor.close()
    return {'data': info}

@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern():
    connection = sql_conetion.Sql_connector()
    connection.cursor.execute(dal.get_customers_payments_by_lastname_pattern())
    info = connection.cursor.fetchall()
    connection.cursor.close()
    return {'data': info}
