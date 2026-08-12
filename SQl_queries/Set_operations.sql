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
