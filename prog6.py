# Sample Data
# employees.txt (stored in HDFS at /user/cloudera/employees.txt)
# 101,John,30,1,50000
# 102,Sam,28,2,60000
# 103,Anna,32,1,75000
# 104,David,29,3,62000
# 105,Lily,27,2,58000

# departments.txt (stored in HDFS at /user/cloudera/departments.txt)
# 1,HR
# 2,Finance
# 3,IT


# Pig Latin Script
# Save the script as employee_analysis.pig and execute it in Cloudera.

-- Load the employees dataset
employees = LOAD 'hdfs://localhost:9000/user/cloudera/employees.txt'
USING PigStorage(',')
AS (emp_id:int, name:chararray, age:int, dept_id:int, salary:int);


-- Load the departments dataset
departments = LOAD 'hdfs://localhost:9000/user/cloudera/departments.txt'
USING PigStorage(',')
AS (dept_id:int, dept_name:chararray);


-- 1. FILTER: Select employees with age greater than 28
filtered_employees = FILTER employees BY age > 28;


-- 2. PROJECT: Select only emp_id, name, and salary columns
projected_employees = FOREACH filtered_employees GENERATE emp_id, name, salary;


-- 3. SORT: Order employees by salary in descending order
sorted_employees = ORDER projected_employees BY salary DESC;


-- 4. GROUP: Group employees by department ID
grouped_by_department = GROUP employees BY dept_id;


-- 5. JOIN: Join employees with department names using dept_id
joined_data = JOIN employees BY dept_id, departments BY dept_id;


-- STORE results in HDFS
STORE sorted_employees INTO 'hdfs://localhost:9000/user/cloudera/output/sorted_employees' USING PigStorage(',');

STORE grouped_by_department INTO 'hdfs://localhost:9000/user/cloudera/output/grouped_by_department' USING PigStorage(',');

STORE joined_data INTO 'hdfs://localhost:9000/user/cloudera/output/joined_data' USING PigStorage(',');


-- DISPLAY the results on the screen
DUMP sorted_employees;

DUMP grouped_by_department;

DUMP joined_data;


# Upload the data in HDFS
hdfs dfs -mkdir -p /user/cloudera


hdfs dfs -put employees.txt /user/cloudera/


hdfs dfs -put departments.txt /user/cloudera/


# Run the Script
pig -x mapreduce employee_analysis.pig


# Output commands
hdfs dfs -cat /user/cloudera/output/sorted_employees/part-r-00000


hdfs dfs -cat /user/cloudera/output/grouped_by_department/part-r-00000


hdfs dfs -cat /user/cloudera/output/joined_data/part-r-00000
