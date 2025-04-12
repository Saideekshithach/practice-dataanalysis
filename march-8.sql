create database microservices;
create table students(
student_id int primary key,
name varchar(100),
age int,
check(age>18));
create table enrollments(
enrollment_id int primary key,
student_id int,
course_id int,
foreign key (student_id) references students(student_id));
insert into students values (1,'saideekshitha',22);
insert into students values(2,'Lavanya',26);
select * from students;
insert into enrollments values(101,1,250);
select * from enrollments;
insert into enrollments values(102,2,252);
select * from enrollments;
create table orderdetails(order_id int,product_id int,quantity int,primary key(order_id,product_id));
desc orderdetails;
insert into orderdetails values(1,101,100);
select * from orderdetails;



