create database javafs;
use javafs;
create table employees(employee_id int auto_increment primary key,first_name varchar(10),last_name varchar(10),department varchar(50),salary decimal(10,2),hire_date Date);
create view sales_employees as select employee_id,first_name,last_name,salary from employees where department='sales';
select * from sales_Employees;
INSERT INTO employees (first_name, last_name, department, salary, hire_date)
VALUES
('Alice', 'Smith', 'HR', 55000.75, '2022-03-15'),
('Bob', 'Johnson', 'IT', 72000.50, '2021-06-01'),
('Charlie', 'Lee', 'Finance', 63000.00, '2020-09-10'),
('Dana', 'White', 'Marketing', 58000.25, '2023-01-20'),
('Ethan', 'Wong', 'Sales', 67000.80, '2019-12-05');
select * from employees;

select * from sales_employees;
update employees set hire_date='2023-04-06' where department="sales";
select * from sales_employees;
update employees set last_name="kong" where first_name="ethan";
select * from Employees;
select * from sales_Employees;



