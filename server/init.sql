"isbn13", "author", "title", "publisher", "pubdate", "price", "binding", "alt", "author_intro", "summary"

CREATE DATABASE dushu DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

create table dushu.book_information(
    id int primary key auto_increment,
    isbn13 varchar(20) comment 'ISBN号',
    author varchar(60) comment '作者',
    translator varchar(20) comment '翻译者',
    title varchar(100) comment '书籍名称',
    publisher varchar(60) comment '出版社',
    pubdate varchar(30) comment '出版时间',
    price varchar(30) comment '书本定价',
    binding varchar(30) comment '装订类别',
    alt varchar(100) comment '豆瓣地址',
    author_intro text comment '作者简介',
    summary text comment '书籍简介',
    add_time date comment '添加时间',
    addr_id varchar(4) comment '书籍位置'
) character set = utf8;

create table dushu.rating(
    id int primary key auto_increment,
    isbn13 varchar(20) comment 'ISBN号',
    max varchar(10) comment '最高分',
    numRaters varchar(10) comment '评价者数量',
    average varchar(10) comment '平均分',
    min varchar(10)
) character set = utf8;

create table dushu.images(
    id int primary key auto_increment,
    isbn13 varchar(20) comment 'ISBN号',
    small varchar(100) comment '小图片',
    large varchar(100) comment '大图片',
    medium varchar(100) comment '中图片'
) character set = utf8;

create table dushu.tags(
    id int primary key auto_increment,
    isbn13 varchar(20) comment 'ISBN号',
    count varchar(10) comment '参与人数',
    name varchar(20) comment '标签名称',
    title varchar(20) comment '标签title'
) character set = utf8;

create table dushu.address(
    id int primary key auto_increment,
    address varchar(200) comment '书籍地址'
) character set = utf8;