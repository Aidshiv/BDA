CREATE DATABASE IF NOT EXISTS company;
USE company;
CREATE TABLE employees (id INT, name STRING, department STRING, salary INT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;
LOAD DATA INPATH '/user/cloudera/data/employees.csv' INTO TABLE employees;
SELECT * FROM employees;
SELECT department, MAX(salary) AS highest_salary FROM employees GROUP BY department;
SELECT * FROM employees WHERE salary > 65000;
SELECT department, COUNT(*) AS employee_count FROM employees GROUP BY department;
