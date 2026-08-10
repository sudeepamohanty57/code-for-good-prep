-- =========================================
-- DDL - Data Definition Language
-- =========================================

-- CREATE TABLE

CREATE TABLE persons(
	id INT NOT NULL,
	first_name VARCHAR (50) NOT NULL,
	birth_date DATE,
	phone VARCHAR (15),
	CONSTRAINT pk_person PRIMARY KEY (id)
)

--ALTER TABLE

ALTER TABLE persons
ADD email VARCHAR(50) NOT NULL

-- DROP
-- Delete the table persons from the database

DROP TABLE persons

