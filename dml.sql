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

