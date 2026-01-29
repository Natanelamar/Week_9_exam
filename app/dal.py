from typing import List, Dict, Any

def get_customers_by_credit_limit_range():
   return """"SELECT customerName, creditLimit 
    FROM customers 
    WHERE creditLimit < 10000 OR creditLimit > 100000; """


def get_orders_with_null_comments():
    return """SELECT orderNumber, comments
    FROM orders
    WHERE comments IS NULL
    order by orderDate;"""
    
#שאלה 3
def get_first_5_customers():
    return """SELECT  C.customerName, E.lastName ,E.firstName
    FROM customers C 
    JOIN employees E ON E.lastName = C.contactLastName
    GROUP BY C.customerName
    ORDER BY E.lastName 
    LIMIT 5;"""
   

def get_payments_total_and_average():
    return """SELECT sum(amount) as sum_payments, avg(amount) as avg_amount, min(amount) as min_amount , max(amount) as max_amount
     FROM payments;"""
    

def get_employees_with_office_phone():
    return """SELECT E.firstName, E.lastName, O.phone
    FROM employees E
    JOIN offices O on O.officeCode = E.officeCode;"""
  
    
#שאלה 6
def get_customers_with_shipping_dates():
   return """SELECT C.customerName, O.orderDate
   FROM customers C
   JOIN orders O on C.customerNumber = O.customerNumber
   GROUP BY C.customerName; 
   """
   
#שאלה 7
def get_customer_quantity_per_order():
    return """SELECT C.customerName, D.quantityOrdered
    FROM customers C
    JOIN orders O on C.customerNumber = O.customerNumber
    JOIN orderdetails D ON D.orderNumber = O.orderNumber
    GROUP BY C.customerName
    ORDER BY C.customerName;
    """


def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    return """SELECT C.customerName, E.firstName, SUM(P.amount)
    FROM customers C
    JOIN employees E on E.lastName = C.contactLastName
    JOIN payments P ON P.customerNumber = C.customerNumber
    WHERE C.contactFirstName LIKE '%Mu%' or C.contactFirstName LIKE '%ly%'
    GROUP BY C.customerName
    ORDER BY SUM(P.amount) DESC;"""