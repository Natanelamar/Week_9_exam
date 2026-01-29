from typing import List, Dict, Any

def get_customers_by_credit_limit_range(cnx):
    """Return customers with credit limits outside the normal range."""
    query = '''SELECT c.customerName, c.creditLimit
                FROM customers c
                WHERE c.creditLimit < 10000 OR c.creditLimit > 100000'''
    
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_orders_with_null_comments(cnx):
    """Return orders that have null comments."""
    query = '''SELECT o.orderNumber, o.comments
                FROM orders o 
                WHERE o.comments IS NULL
                ORDER BY o.orderDate'''
    
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_first_5_customers(cnx):
    """Return the first 5 customers."""
    query = '''SELECT c.customerName, c.contactLastName, c.contactFirstName
                FROM customers c 
                ORDER BY c.contactLastName 
                LIMIT 5'''
    
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_payments_total_and_average(cnx):
    """Return total and average payment amounts."""
    query = '''SELECT SUM(p.amount), AVG(p.amount), MIN(p.amount), MAX(p.amount)
                FROM payments p'''
    
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_employees_with_office_phone(cnx):
    """Return employees with their office phone numbers."""
    query = '''SELECT e.firstName, e.lastName, o.phone phoneOffice
                FROM employees e LEFT JOIN offices o 
                ON e.officeCode = o.officeCode'''
    
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_customers_with_shipping_dates(cnx):
    """Return customers with their order shipping dates."""
    query = '''SELECT c.customerName, o.shippedDate
                FROM customers c JOIN orders o 
                ON c.customerNumber = o.customerNumber'''
    
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_customer_quantity_per_order(cnx):
    """Return customer name and quantity for each order."""
    query = '''SELECT c.customerName, SUM(od.quantityOrdered)
                FROM customers c JOIN orders o 
                ON c.customerNumber = o.customerNumber JOIN orderdetails od 
                ON o.orderNumber = od.orderNumber 
                GROUP BY o.orderNumber, c.customerName
                ORDER BY c.customerName'''
    
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_customers_payments_by_lastname_pattern(cnx):
    """Return customers and payments for last names matching pattern."""
    query = '''SELECT c.customerName, CONCAT(e.firstName, e.lastName), SUM(p.amount) 
                FROM customers c JOIN employees e 
                ON c.salesRepEmployeeNumber = e.employeeNumber JOIN payments p
                ON c.customerNumber = p.customerNumber 
                WHERE c.contactFirstName LIKE '%Mu%' OR c.contactFirstName LIKE '%ly%' 
                GROUP BY c.customerName
                ORDER BY SUM(p.amount) DESC'''
    
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data
