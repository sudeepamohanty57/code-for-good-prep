/* STRING FUNCTIONS */

/* MANIPULATION */

-- CONCAT

-- show a list of customers' first name together with their country in one column

SELECT
	first_name,
	country,
	CONCAT(first_name, '-' , country) AS name_country
FROM customers

-- UPPER & LOWER

SELECT
	first_name,
	country,
	LOWER(first_name) AS low_name,
	UPPER(first_name) AS up_name
FROM customers

--TRIM 
-- Find customers whose first name contains leading or trailing spaces

SELECT 
	first_name
FROM customers
WHERE first_name!= TRIM(first_name)

--REPLACE
-- Remove dashes (-) from a phone number

SELECT
'123-456-7890' AS phone,
REPLACE ('123-456-7890', '-', '') As clean_phone

-- Replace File extence from txt to csv

SELECT
'report.txt' As old_filename,
REPLACE('report.txt', '.txt','.csv') AS new_filename

/* CALCULATION */

-- LEN
-- calculate the lengthof each customers' first_name

SELECT
	first_name,
	LEN(first_name) AS len_name
FROM customers

/* STRING EXTRACTION */

-- LEFT & RIGHT
-- Retrive the first two characters of each first name.

SELECT
	first_name,
	LEFT(TRIM(first_name), 2) AS first_2_char
FROM customers

-- Retrive the last two characters of each first name.

SELECT
	first_name,
	RIGHT(first_name, 2) AS last_2_char
FROM customers

-- SUBSTRING

--Retrive a list of customers' first name removing the first character.

SELECT
	first_name,
	SUBSTRING(TRIM(first_name), 2, LEN(first_name)) AS sub_name
FROM customers