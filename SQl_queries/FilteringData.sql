-- COMPARISION operators
-- Retrive all customers from Germany

SELECT *
FROM customers
WHERE country = 'Germany'

-- Retrive all customers who are not from Germany

SELECT *
FROM customers
WHERE country != 'Germany'

-- Retrive all customers with a score greater than 500

SELECT *
FROM customers
WHERE score > 500

-- Retrive all customers with a score of 500 or more

SELECT *
FROM customers
WHERE score >= 500

--========================================================================

-- LOGICAL operators

--AND
/* Retrive all customers who are from USA 
and have a score greater athan 500.*/

SELECT *
FROM customers
WHERE country = 'USA' AND score > 500

--OR
/* Retrive all customers who are either from USA 
or have a score greater athan 500.*/

SELECT *
FROM customers
WHERE country = 'USA' OR score >500

--NOT
-- Retrive all customers with a score not less than 500

SELECT *
FROM customers
WHERE NOT score < 500

--========================================================================

--RANGE operator

--BETWEEN 
/* Retrive all customers whose score falls 
in the range between 100 and 500 */

SELECT *
FROM customers
WHERE score BETWEEN 100 AND 500

--========================================================================

-- MEMBERSHIP operators

--IN
-- Retrive all customers from either Germany or USA
SELECT *
FROM customers
WHERE country IN ('Germany' , 'USA')

--NOT IN

SELECT *
FROM customers
WHERE country NOT IN ('USA', 'UK')

--========================================================================

-- SEARCH operator

--LIKE
-- Find all customers whose first name starts with 'M'

SELECT *
FROM customers
WHERE first_name LIKE 'M%' 

-- Find all customers whose first name ends with 'n'

SELECT *
FROM customers
WHERE first_name LIKE '%n'

--Find customers whose name contains a r

SELECT *
FROM customers
WHERE first_name LIKE '%r%'

--Find all customers whose first name has 'r' in the 3rd positio

SELECT *
FROM customers
WHERE first_name LIKE '__r%'