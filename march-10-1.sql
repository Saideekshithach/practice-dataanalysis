use dataanalytics;
create table users(user_id int auto_increment,name varchar(100),primary key(user_id));
alter table users auto_increment=1001;
select * from orders;
create table ord(id int unsigned,customer_name varchar(20),coupon_code varchar(20)); 
insert into ord values(1,'sai','c12'),(2,'ramya','s12');
select id,customer_name,coalesce(coupon_code,'default') as applied_coupon from ord;
insert into ord(id,customer_name) values(3,'srija');
select id,customer_name,coalesce(coupon_code,'default') as applied_coupon from ord;
start transaction;
savepoint point;
insert into products values(8,'honda',500000);
select * from products;
rollback to point;
commit;
select * from products;
start transaction;
savepoint point;
insert into products values(9,'ABC',8800000);
insert into products values(10,'CFG',1000000);
rollback to point;
commit;
select * from products;
delimiter //
create procedure getallusers()
begin
select * from users;
end;
//
call getallusers();
select * from customers;
delimiter //
create procedure getuserdetail(in user_id int)
begin 
select customer_id,name from customers where customer_id=user_id;
end;
//
call getuserdetail(5);
select * from users;
delimiter //
create procedure getusernames4(in id int,out names varchar(100))
begin
select name into names from users where user_id=id;
end;
 //
delimiter ;
set @names='';
call getusernames4(1,@names);
select @names;
select @user_id;
select * from users;
insert into users values(1,'deekshitha');


