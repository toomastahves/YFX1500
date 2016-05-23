# Tables
create table books (
    bookid int not null primary key auto_increment,
    title varchar(100) not null,
    author varchar(100) not null,
    onloan boolean,
    duedate date,
    borrowerid int,
    foreign key (borrowerid) references borrowers(borrowerid)
) engine = innodb;

create table borrowers (
    borrowerid int not null primary key auto_increment,
    name varchar(100) not null,
    address varchar(100) not null
) engine = innodb;

# Data
insert into borrowers values
(100, 'Homer Simpson', 'Springfield'),
(101, 'Daenerys', 'Dragonstone'),
(102, 'Tyrion', 'Kings Landing');

insert into books values
(null, 'Dune', 'Pratchett', false, null, null),
(null, 'Iron Throne', 'Gandalf', false, null, null),
(null, 'Best Man', 'Barney', false, null, null);

UPDATE books SET onloan = 1, duedate = '2016-05-31', borrowerid = 100 WHERE books.bookid = 1;

SELECT books.title, borrowers.name from books, borrowers where books.borrowerid = borrowers.borrowerid;

# Procedure
DELIMITER $$
CREATE PROCEDURE `library`.`overdue_books` ()
BEGIN
    SELECT * FROM books where duedate < current_date;
END

# Function
DELIMITER $$
CREATE FUNCTION `library`.`count_overdue_books` (days integer)
RETURNS INTEGER
BEGIN
    return (
        SELECT count(*) FROM books WHERE duedate < date_sub(current_date(), interval days day)
    );
END

# Users
create user 'borrower'@'localhost' identified by 'borrower';
grant select on library.books to 'borrower'@'localhost';
show grants for borrower@'localhost';

create user 'librarian'@'localhost' identified by 'librarian';
grant select, insert, delete, update on library.* to 'librarian'@'localhost';

create user 'assistant'@'localhost' identified by 'assistant';
grant select on library.* to 'assistant'@'localhost';
grant update (`onloan`, `duedate`, `borrowerid`) on library.books to 'assistant'@'localhost';
