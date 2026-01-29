from typing import List, Dict, Any
from app.db import get_db_connection


def get_customers_by_credit_limit_range():
    conn = get_db_connection()
    cursor = conn.cursor()
    query1 = """
    SELECT `customerName`,`creditLimit`
        from customers
        where `creditLimit` < 10000 or creditLimit > 100000
    """
    cursor.execute(query1)
    q = cursor.fetchall()
    cursor.close()
    conn.close()
    return q



def get_orders_with_null_comments():
    conn = get_db_connection()
    cursor = conn.cursor()
    query2 = """
    SELECT `orderNumber`,`comments`,`orderDate` FROM `orders` 
    WHERE comments is null
    order by `orderDate` DESC
    """
    cursor.execute(query2)
    q = cursor.fetchall()
    cursor.close()
    conn.close()
    return q


def get_first_5_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    query3 = """SELECT
    `customerName`,`contactLastName`,`contactFirstName`
    FROM `customers`
    order by `contactLastName` LIMIT 5"""
    
    cursor.execute(query3)
    q = cursor.fetchall()
    cursor.close()
    conn.close()
    return q


def get_payments_total_and_average():
    conn = get_db_connection()
    cursor = conn.cursor()
    query4 = """SELECT
    SUM(`amount`) as sum,
    avg(`amount`)as avg,
    MIN(`amount`)as min,
    MAX(`amount`)as max
    FROM `payments`
    """
    cursor.execute(query4)
    q = cursor.fetchall()
    cursor.close()
    conn.close()
    return q


def get_employees_with_office_phone():
    conn = get_db_connection()
    cursor = conn.cursor()
    query5 = """SELECT employees.firstName, employees.lastName, offices.phone
    FROM employees
    JOIN offices ON employees.officeCode = offices.officeCode;"""

    cursor.execute(query5)
    q = cursor.fetchall()
    cursor.close()
    conn.close()
    return q


def get_customers_with_shipping_dates():
    conn = get_db_connection()
    cursor = conn.cursor()
    query6 = """SELECT cust.customerName, of.shippedDate,
    (SELECT AVG(quantityOrdered) FROM orderdetails) AS total_avg
    FROM customers cust
    LEFT JOIN orders of ON cust.customerNumber = of.customerNumber;"""

    cursor.execute(query6)
    q = cursor.fetchall()
    cursor.close()
    conn.close()
    return q


def get_customer_quantity_per_order():
    conn = get_db_connection()
    cursor = conn.cursor()
    query7 = """SELECT
    c.customerName,
    od.quantityOrdered
    FROM customers c
    INNER JOIN orders o ON c.customerNumber = o.customerNumber
    INNER JOIN orderdetails od ON o.orderNumber = od.orderNumber
    ORDER BY c.customerName ASC, c.contactLastName ASC;
    """
    
    cursor.execute(query7)
    q = cursor.fetchall()
    cursor.close()
    conn.close()
    return q


def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    conn = get_db_connection()
    cursor = conn.cursor()
    query8 = """SELECT
    c.customerName,
    e.firstName AS salesmanFirstName,
    SUM(p.amount) AS totalPayments
    FROM customers c
    JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
    JOIN payments p ON c.customerNumber = p.customerNumber
    WHERE e.firstName LIKE '%Mu%' OR e.firstName LIKE '%ly%'
    GROUP BY c.customerName, e.firstName
    ORDER BY totalPayments DESC;
    """
    cursor.execute(query8)
    q = cursor.fetchall()
    cursor.close()
    conn.close()
    return q
