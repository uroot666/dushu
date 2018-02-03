"isbn13", "author", "title", "publisher", "pubdate", "price", "binding", "alt", "author_intro", "summary"

CREATE DATABASE dushu DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

create table dushu.book_information(
    id int primary key auto_increment,
    isbn13 varchar(20) comment 'ISBN号',
    author varchar(60) comment '作者',
    title varchar(100) comment '书籍名称',
    publisher varchar(60) comment '出版社',
    pubdate varchar(30) comment '出版时间',
    price varchar(30) comment '书本定价',
    binding varchar(30) comment '装订类别',
    alt varchar(100) comment '豆瓣地址',
    author_intro text comment '作者简介',
    summary text comment '书籍简介'
) character set = utf8;