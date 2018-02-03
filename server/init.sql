"isbn13", "author", "title", "publisher", "pubdate", "price", "binding", "alt", "author_intro", "summary"

CREATE DATABASE dushu DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

create table dushu.book_information(
    id int primary key auto_increment,
    isbn13 varchar(20),
    author varchar(60),
    title varchar(100),
    publisher varchar(60),
    pubdate varchar(30),
    price varchar(30),
    binding varchar(30),
    alt varchar(100),
    author_intro text,
    summary text
) character set = utf8;