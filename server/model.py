# encoding: utf-8
# 功能模块

import requests
import json

import dbutil

book_storage_sql = 'insert into book_information(isbn13, author, title, publisher, pubdate, price, binding, alt, author_intro, summary) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
book_storage_key = ["isbn13", "author", "title", "publisher", "pubdate", "price", "binding", "alt", "author_intro", "summary"]
book_storage_value_list = ["rating", "tags", "images", ]

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
        if res.get('title', '') :
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
    book_list = []
    for key in book_storage_key:
        if key == 'catalog':
            continue
        elif key == "author":
            book_list.append(book_dict.get(key)[0])
        else:
            book_list.append((book_dict.get(key, '')))
    dbutil.db_operating(book_storage_sql, False, book_list)
    # print(book_list)
    return {'code':0}

# 判断书籍是否已经在仓库
def book_is_storage(isbn):
    return True