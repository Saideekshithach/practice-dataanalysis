create database DataAnalytics;
use DataAnalytics;
create table persons(
personid int,
lastname varchar(255),
firstname varchar(255),
address varchar(255),
city varchar(255)
);
insert into persons values(1,'Chetlapalle','Saideekshitha',
'Apartment','chennai');
insert into persons values(2,'gudipati','soujanya','nallagunta'
,'hyderabad');
insert into persons values(3,'devarapalle','Sravani',
'Westmombalam','chennai');
select * from persons;
delete from persons where personid=3;
 set sql_safe_updates=0;
 select * from persons;
 insert into persons values(3,'devarapalle','Sravani',
 'Westmambalam','chennai');
 update persons set address="diluskhnagar" where personid=2;
 select * from persons;
 create table users(
 userid int auto_increment primary key,
 username varchar(50) unique not null,
 email varchar(100) unique not null,
 passwordHash varchar(255) not null,
 firstname varchar(50),
 lastname varchar(50),
 dateofbirth date,
 createdate datetime default current_timestamp,
 lastlogin datetime,
 status enum('active','inactive','suspended') default 'active',
 index (email));
 desc users;
 insert into users values(1,'sai','sai12@gmail.com','sai@123','sai','deekshitha','2002-09-21'
 ,now(),now(),'active');
 select * from users;
 insert into users values(2,'Sravani','sravani88@gmail.com','sravs12','sravani','devarapalle','1988-08-29'
 ,now(),now(),'active');
 
 
 