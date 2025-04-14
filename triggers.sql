create table items(id int primary key,name varchar(255) not null,price decimal(10,2) not null);
insert into items(id,name,price) values(1,'fruits',100.00);
select * from items;
create table item_changes(change_id int primary key 
auto_increment,item_id int,change_type varchar(10),
change_timestamp timestamp default current_timestamp,
foreign key (item_id) references items(id));
delimiter ??
create trigger update_changes after update on items for each row begin insert 
into item_changes(item_id,change_type) values(new.id,'update');
end;
??

select * from item_changes;
update items set name="Laptop" where id=1
select * from items;