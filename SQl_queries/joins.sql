/* COMBINING DATA */
/* (BASIC) */
--JOINS

-- NO JOIN

/* Retrive all data from customers and orders
in two different results */

SELECT *
FROM customers;

SELECT *
FROM orders;

-- INNER JOIN

/* Get all customers along with their orders,
but only for customers who have placed an order */

SELECT *
FROM customers
INNER JOIN orders
ON id = customer_id

-- BEST practice(better version)

SELECT 
	c.id,
	c.first_name,
	o.order_id,
	o.sales
FROM customers AS c
INNER JOIN orders AS o
ON c.id = o.customer_id

-- LEFT JOIN

/* Get all customers along with their orders,
including those without orders. */

SELECT 
	c.id,
	c.first_name,
	o.order_id,
	o.sales
FROM customers AS c
LEFT JOIN orders AS o
ON c.id = o.customer_id

-- RIGHT JOIN

/* Get all customers along with their orders,
including orders without matching customers . */

SELECT 
	c.id,
	c.first_name,
	o.order_id,
	o.sales
FROM customers As c
RIGHT JOIN orders AS o
ON c.id = o.customer_id

/* ALTERNATIVE ising LEFT join (Better practice) */

SELECT 
	c.id,
	c.first_name,
	o.order_id,
	o.sales
FROM orders AS o
LEFT JOIN customers AS c
ON c.id = o.customer_id

-- FULL JOIN 

/* Get all customers and all orders, even if there's no match. */

SELECT
	c.id,
	c.first_name,
	o.order_id,
	o.sales
FROM customers AS c
FULL JOIN orders AS o
ON c.id = o.customer_id


/* (ADVANCED) */

-- LEFT ANTI JOIN

/* Get all customers who haven't place any order */

SELECT *
FROM customers AS c
LEFT JOIN orders AS o
ON c.id = o.customer_id
WHERE o.customer_id IS NULL

-- RIGHT ANTI JOIN

/* Get all orders without matching customers */

SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
ON c.id = o.customer_id
WHERE c.id IS NULL

/* ALTERNATIVE ising LEFT ANTI join (Better practice) */

SELECT *
FROM orders AS o
LEFT JOIN customers AS c
ON c.id = o.customer_id
WHERE c.id IS NULL

-- FULL ANTI JOIN

/* Find customers without orders and orderswithout customers */

SELECT *
FROM customers AS c
FULL JOIN orders As o
ON c.id = o.customer_id
WHERE c.id IS NULL OR o.customer_id IS NULL

/* TASK */

/* Get all customers along with their orders,
but only for customers who have placed an order
(WITHOUT using INNER JOIN) */

SELECT *
FROM customers As c
LEFT JOIN orders As o
ON c.id = o.customer_id
WHERE o.customer_id IS NOT NULL

-- CROSS JOIN 

/* Generate all possible combinations of customers 
and orders */   

SELECT *
FROM customers
CROSS JOIN orders


/* JOINING MULTIPLE TABLES */

/* TASK */

USE SalesDB

/* Using SalesDB, Retrive a list of all orders, along with the related customer,
product, and employee details. for each order, dispaly:
 OrderID, Customer's name, Product name, Sales, Price, Sales person's name */

SELECT 
	o.OrderID,
	o.Sales,
	c.FirstName AS CustomerFirstName,
	c.LastName AS CustomerLastName,
	p.Product As ProductName,
	p.Price,
	e.FirstName AS EmployeeFirstName,
	e.LastName AS EmployeeLastName
FROM Sales.Orders As o
LEFT JOIN Sales.Customers As c
ON o.CustomerID = c.CustomerID

LEFT JOIN Sales.Products As p
ON o.ProductID = p.ProductID

LEFT JOIN Sales.Employees As e
ON o.SalesPersonID = e.EmployeeID

