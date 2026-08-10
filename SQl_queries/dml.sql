-- =========================================
-- DML - Data Manipulation Language
-- =========================================


-- INSERT by manually entering values

INSERT INTO customers (id, first_name, country, score)
VALUES 
	(6, 'Anna', 'USA', NULL),
	(7, 'Sam', NULL, 100)
		

-- INSERT using SELECT
-- copy data from 'customers' table into 'persons'

INSERT INTO persons (id, person_name, birth_date, phone)
SELECT
	id,
	first_name,
	NULL,
	'Unknown'
FROM customers


--UPDATE table
-- change the score of customer 6 to 0

UPDATE customers
SET score=0
WHERE id=6

-- change the score of customer with id 7 to 0 and update country to 'UK'

UPDATE customers
SET score=0,
	country='UK'
WHERE id=7

--DELETE FROM table

DELETE FROM customers
where id>5

--delete all the values from the table
TRUNCATE TBALE persons