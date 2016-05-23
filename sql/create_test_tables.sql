use test;

create table table1 (id int, value varchar(10));
insert into table1 (id, value) values (1, 'first');
insert into table1 (id, value) values (2, 'second');
insert into table1 (id, value) values (3, 'third');
insert into table1 (id, value) values (4, 'fourth');
insert into table1 (id, value) values (5, 'fifth');

create table table2 (id int, value varchar(10));
insert into table2 (id, value) values (1, 'first');
insert into table2 (id, value) values (2, 'second-2');
insert into table2 (id, value) values (3, 'third');
insert into table2 (id, value) values (6, 'sixth');
insert into table2 (id, value) values (7, 'seventh');
insert into table2 (id, value) values (8, 'eight');

create table employee (employeeid int primary key, name nvarchar(50), managerid int);
insert into employee values (1, 'mike', 3);
insert into employee values (2, 'david', 3);
insert into employee values (3, 'roger', null);
insert into employee values (4, 'marry', 2);
insert into employee values (5, 'joseph', 2);
insert into employee values (7, 'ben', 2);

