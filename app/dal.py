from typing import List, Dict, Any

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    query = '''SELECT c.customerName, c.creditLimit
                FROM customers c
                WHERE c.creditLimit < 10000 OR c.creditLimit > 100000'''
    return query

def get_orders_with_null_comments():
    """Return orders that have null comments."""
    query = '''SELECT o.orderNumber, o.comments
                FROM orders o 
                WHERE o.comments IS NULL'''
    return query

def get_first_5_customers():
    """Return the first 5 customers."""
    # SELECT c.customerName, c.contactLastName, c.contactFirstName, 
    # FROM customers c 
    # ORDER BY c.
    query = ''''''
    return query

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    query = ''''''
    return query

def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    query = '''SELECT e.firstName, e.lastName, o.phone phoneOffice
                FROM employees e LEFT JOIN offices o 
                ON e.officeCode = o.officeCode'''
    return query

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    query = ''''''
    return query

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    query = ''''''
    return query

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    query = '''SELECT c.customerName, CONCAT(c.contactFirstName, ' ', c.contactLastName) contactName, SUM(p.amount)
                FROM customers c LEFT JOIN payments p 
                ON c.customerNumber = p.customerNumber
                GROUP BY c.customerName
                WHERE c.contactFirstName LIKE '%Mu%' OR c.contactFirstName LIKE '%ly%'''
    return query
