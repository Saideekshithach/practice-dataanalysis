use javafs;
delimiter ??
create function rectanglearea(length float,width float)
returns float
deterministic
begin
return length*width;
end ??

delimiter ;
select rectanglearea(2.2,2.1) as area;
 delimiter // 
 create function mulnumber(a int,b int)
 returns int
 deterministic
 begin
 return a*b;
 end //
 delimiter ;
 select mulnumber(5,6) as multiplication;
