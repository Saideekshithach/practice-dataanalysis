use dataanalytics;
select * from employees;
select ename from employees where salary<(Select avg(Salary) from employees);
select * from employees;
select avg(Salary) from employees;
CREATE TABLE departments (

    department_id INT PRIMARY KEY,

    department_name VARCHAR(50)

);
 
CREATE TABLE employees (

    employee_id INT PRIMARY KEY,

    employee_name VARCHAR(50),

    department_id INT,

    FOREIGN KEY (department_id) REFERENCES departments(department_id)

);
INSERT INTO departments (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Marketing'),
(3, 'HR');
INSERT INTO employees (employee_id, employee_name, department_id) VALUES
(101, 'Alice', 1),
(102, 'Bob', 1),
(103, 'Charlie', 2),
(104, 'Diana', 3);
rename table employees to emp;
select employee_name from employees where department_id in (select department_id from departments where department_name="sales");
select employee_name,(Select department_name from departments where departments.department_id=employees.department_id) as department_name from employees;
select count(*) from employees;
select count(*) from employees group by department_id;
select department_id from employees group by department_id having count(*)>1;
select employee_name,department_id from employees where department_id in(select department_id from employees group by department_id having count(*)>1);
 select employee_name,department_id from employees where department_id in(select department_id,count(*) from employees group by department_id having count(*)>1);
 select department_id,department_name from departments d where exists(Select 1 from employees e where e.department_id=d.department_id);
 insert into departments(department_id,department_name) values(4,'Training');
 select * from departments;
 select * from employees;
 select department_name from departments d where not exists (Select 1 from employees e where e.department_id=d.department_id);
 select * from employees;
 select department_id from employees group by department_id having avg(employee_id)>102;
 select department_id from employees group by department_id having avg(employee_id)>102;
 select ucase('Hello world') as uppercase_String;
 select lcase('Hello world') as lowercase_string;
 select mid('Hello world',4,8)as sub_String;
 select length('hello world') as string_length;
 select round(1560.4444,2) as round_value;
 select now() as currentDateTime;
 select employee_name,length(employee_name) as namelength from employees;
 select * from products;
 select productname,price,round(price) as rounded_price from products;
 
 