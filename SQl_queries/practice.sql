CREATE TABLE beneficiaries (
    beneficiary_id INT PRIMARY KEY,
    name VARCHAR(100),
    district VARCHAR(50)
)

CREATE TABLE donations (
    donation_id INT PRIMARY KEY,
    beneficiary_id INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (beneficiary_id)
    REFERENCES beneficiaries(beneficiary_id)
)

SELECT district,
    COUNT(*) AS beneficiaries_count
FROM beneficiaries
GROUP BY district
ORDER BY beneficiaries_count DESC

SELECT COUNT(*) AS total_beneficiaries
FROM beneficiaries

/*Write a SQL query to display the name of each beneficiary along with 
the amount of each donation they have received.*/

SELECT
    b.name,
    d.amount
FROM beneficiaries AS b
LEFT JOIN donations As d
ON b.beneficiary_id= d.beneficiary_id

/* Write a SQL query to display each beneficiary's name along with the
 total amount of donations they have received. If a beneficiary has
  received multiple donations, calculate their total donation amount. */

SELECT 
    b.name,
    SUM(d.amount) AS donation_amt
FROM beneficiaries AS b
LEFT JOIN donation AS d
ON b.beneficiary_id= d.beneficiary_id
GROUP BY b.beneficiary_id, b.name 

/* Modify your Q7 query so that beneficiaries who have received 
no donations are also displayed, with their total donation shown 
as 0 instead of NULL. */

SELECT 
    b.name,
    COALESCE(SUM(d.amount), 0) AS donation_amt
FROM beneficiaries AS b
LEFT JOIN donations AS d
ON b.beneficiary_id = d.beneficiary_id
GROUP BY b.beneficiary_id, b.name;

/* Modify the Q8 query so that the beneficiaries are displayed in 
descending order of their total donation amount, with the highest 
donor appearing first. */

SELECT 
    b.name,
    COALESCE(SUM(d.amount), 0) AS donation_amt
FROM beneficiaries AS b
LEFT JOIN donations AS d
ON b.beneficiary_id = d.beneficiary_id
GROUP BY b.beneficiary_id, b.name
ORDER BY donation_amt DESC

/* Write a SQL query to calculate the total amount of donations 
received by each district. */

SELECT 
    b.district,
    COALESCE(SUM(d.amount), 0) AS donation_amt
FROM beneficiaries AS b
LEFT JOIN donations AS d
ON b.beneficiary_id = d.beneficiary_id
GROUP BY b.district

/* Write a SQL query to display only those districts whose total
 donations are greater than ₹10,000. */

 SELECT
    b.district,
    SUM(d.amount) As donation_amt
FROM beneficiaries As b
LEFT JOIN donations AS d
GROUP BY b.districts
HAVING SUM(d.amount) > 10000