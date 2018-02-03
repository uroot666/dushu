# encoding: utf-8
# 功能模块

import requests
import json
import datetime

import dbutil

address_sql = 'select id from address order by id desc limit 1'

book_storage_sql = 'insert into book_information(isbn13, author, translator, title, publisher, pubdate, price, binding, alt, author_intro, summary, add_time, addr_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

book_image_sql = 'insert into images(isbn13, small, large, medium) values (%s, %s, %s, %s)'

book_rating_sql = 'insert into rating(isbn13, max, numRaters, average, min) values (%s, %s, %s, %s, %s)'

book_tags_sql = 'insert into tags(isbn13, count, name, title) values (%s, %s, %s, %s)'

add_address_sql = 'insert into address(address) values (%s)'

book_storage_key = ["isbn13", "author", "translator", "title", "publisher", "pubdate", "price", "binding", "alt", "author_intro", "summary"]
book_storage_value_list = ["rating", "tags", "images"]

# 请求豆瓣API，返回书籍信息
def book_information(barcode):

    headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding": "gzip",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Referer": "http://www.example.com/",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
        }
    url = 'https://api.douban.com/v2/book/isbn/' + barcode
    res={}

    try:
        res = json.loads(requests.get(url, headers=headers).text)
        #写入数据库
        if res.get('title', '') and book_is_storage(res.get('isbn13')):
            code = book_storage(res)
    except BaseException as e:
        print(e)
    finally:
        title = res.get('title', '')
        author = res.get('author', '')
        publisher = res.get('publisher', '')
        pubdate = res.get('pubdate', '')
        price = res.get('price', '')
    return json.dumps({'data':{'title':title, 'author':author, 'publisher':publisher,'pubdate':pubdate, 'price':price}}, ensure_ascii=False)

# 将书籍信息存入数据库
def book_storage(book_dict):
    isbn = book_dict.get('isbn13', '')
    book_list = []
    _rating = [isbn]
    _tags = []
    _images = [isbn]
    _rating_key = ['max', 'numRaters', 'average', 'min']
    _tags_key = ['count', 'name', 'title']
    _images_key = ['small', 'large', 'medium']

    for key in book_storage_key:
        if key == 'catalog':
            continue
        elif key == "author" or key == "translator":
            book_list.append(book_dict.get(key)[0])
        else:
            book_list.append((book_dict.get(key, '')))
    add_time = datetime.datetime.now().strftime("%Y-%m-%d")
    book_list.append(add_time)
    addr_id = book_address()[0][0]
    book_list.append(addr_id)
    
    for key in book_storage_value_list:
        if key == 'rating':
            rating = book_dict.get('rating', '')
            for key in _rating_key:
                _rating.append(rating.get(key, ''))
        elif key == 'tags':
            tags = book_dict.get('tags', '')
            for key in tags:
                _tags.append([isbn, key.get('count', ''), key.get('name', ''), key.get('title', '')])
        elif key == 'images':
            images = book_dict.get('images', '')
            for key in _images_key:
                _images.append(images.get(key, ''))

    dbutil.db_operating(book_storage_sql, False, book_list)
    dbutil.db_operating(book_image_sql, False, _images)
    dbutil.db_operating(book_rating_sql, False, _rating)
    for key in _tags:
        dbutil.db_operating(book_tags_sql, False, key)
    return {'code':0}

# 判断书籍是否已经在仓库
def book_is_storage(isbn):
    return True

def book_address():
    _, addr_id = dbutil.db_operating(address_sql, True)
    return addr_id

def add_address(address):
    dbutil.db_operating(add_address_sql, False, (address,))