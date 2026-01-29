from typing import List, Dict, Any
from db import get_db_connection


def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    query = '''SELECT c.customerName, c.creditLimit
    FROM customers c
    WHERE c.creditLimit < 10000 OR c.creditLimit > 100000'''
    cnx = get_db_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        clean_result = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
    return clean_result


def get_orders_with_null_comments():
    """Return orders that have null comments."""
    query = '''SELECT o.orderNumber, o.comments
    FROM orders o
    WHERE o.comments IS NULL
    ORDER BY o.orderDate
    '''
    cnx = get_db_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        clean_result = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
    return clean_result


def get_first_5_customers():
    """Return the first 5 customers."""
    query = '''SELECT c.customerName, c.contactLastName, c.contactFirstName
        FROM customers c
        ORDER BY c.contactLastName
        LIMIT 5
        '''
    cnx = get_db_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        clean_result = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
    return clean_result


def get_payments_total_and_average():
    """Return total and average payment amounts."""
    query = '''SELECT SUM(p.amount) AS total_amount, AVG(p.amount) AS avg_amount, \
    MIN(p.amount) AS min_amount, MAX(p.amount) AS max_amount
    FROM payments p
    '''
    cnx = get_db_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        clean_result = dict(zip(cursor.column_names, cursor.fetchone()))
    return clean_result


def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    query = '''SELECT e.firstName, e.lastName, o.phone AS office_phone
    FROM employees e INNER JOIN offices o
    ON e.officeCode=o.officeCode'''
    cnx = get_db_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        clean_result = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
    return clean_result


def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    query = '''SELECT c.customerName, o.orderDate
    FROM customers c LEFT OUTER JOIN orders o
    ON c.customerNumber=o.customerNumber
    '''
    cnx = get_db_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        clean_result = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
    return clean_result


def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    pass


def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    pass
