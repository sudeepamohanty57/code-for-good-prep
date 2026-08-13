--==========================================================================================
/*SET OPERATORS */
--==========================================================================================

/* 1. UNION */

-- Combine the data from employee and customersinto one table

SELECT 
	FirstName,
	LastName
FROM Sales.Customers

UNION 

SELECT 
	FirstName,
	LastName
FROM Sales.Employees

/* UNION ALL */
-- combine the data from employees and customers into one table, including duolicates

SELECT 
	FirstName,
	LastName
FROM Sales.Employees

UNION ALL

SELECT 
	FirstName,
	LastName
FROM Sales.Customers

/* EXCEPT */

-- Find the employees who are not customers at the sametime

SELECT 
	FirstName,
	LastName
FROM Sales.Employees

EXCEPT

SELECT
	FirstName,
	LastName
FROM Sales.Customers

/* INTERSECT */

-- Find the employees , who are also customers

SELECT
	FirstName,
	LastName
FROM Sales.Employees

INTERSECT

SELECT 
	FirstName,
	LastName
FROM Sales.Customers

/* UNION USE CASE */

-- Orders data are stored in separate tables (orders and ordersArchive)
-- Combine all orders data into one report without duplicates.

SELECT *
FROM Sales.Orders

UNION

SELECT *
FROM Sales.OrdersArchive

-- * Best practice
--Never use an asterisk(*) to combine tables, list needed columns instead

SELECT
'Orders' As SourceTable
,[OrderID]
,[ProductID]
,[CustomerID]
,[SalesPersonID]
,[OrderDate]
,[ShipDate]
,[OrderStatus]
,[ShipAddress]
,[BillAddress]
,[Quantity]
,[Sales]
,[CreationTime]
FROM [SalesDB].[Sales].[Orders]

UNION 

SELECT 
'OrderArchive' As SourceTable
,[OrderID]
,[ProductID]
,[CustomerID]
,[SalesPersonID]
,[OrderDate]
,[ShipDate]
,[OrderStatus]
,[ShipAddress]
,[BillAddress]
,[Quantity]
,[Sales]
,[CreationTime]
FROM [SalesDB].[Sales].[OrdersArchive]
ORDER BY OrderID




	

