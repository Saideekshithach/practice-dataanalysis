use javafs;
create table employee_Details(employee_id int primary key,name varchar(50),
department varchar(50),salary int);
INSERT INTO employee_details  VALUES
(1, 'Alice',   'Sales', 50000),
(2, 'Bob',     'Sales', 60000),
(3, 'Charlie', 'Sales', 45000),
(4, 'David',   'IT',    70000),
(5, 'Eva',     'IT',    80000),
(6, 'Frank',   'IT',    75000);

insert into employee_details values (7, 'Keifer',   'IT',    75000);
select * from employee_Details;
select employee_id,name,department,salary,row_number() over(partition by department
order by salary desc) as rank_in_dept from employee_Details;
select employee_id,name,department,sum(salary) over (order by salary) as running_total from employee_Details;

select employee_id,name,department,salary,lag(salary) over (order by salary) as previous_Salary,lead(salary) over (order by salary) as next_salary from employee_Details;
select employee_id,name,department,salary,rank() over (partition by department order by salary desc
) as salary_rank from employee_Details;
select employee_id,name,department,salary,dense_rank() over (partition by department order by salary desc
) as salary_rank from employee_Details;
select employee_id,name,department,salary,
 ntile(2) over (order by salary ) as salary_quartile 
 from employee_details;

