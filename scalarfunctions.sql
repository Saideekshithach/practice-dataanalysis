use javafs;
select ucase("sai deekahitha") as uppercasename;
select lcase("sai deekahitha") as lowercasename;
select mid("sai deekshitha",4,9)as substring;
select length("sai deekshitha")as length_name;
select now() as currentdatetime;
select round(12.345,2) as roundedvalue;
select format(12.3456,3) as flooredvalue;
select * from employees;
select * from employee_Details;
select name,length(name) as len from employee_Details;
select employee_id,ucase(name) as employee_names from employee_Details;
select * from items;
select id,round(price,1) from items;

