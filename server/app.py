#encoding: utf-8

from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import redirect

import hashlib
import requests
import json

import model

app = Flask(__name__)


# 用于微信接入认证使用
# @app.route('/weixin/',methods=['GET','POST'])
# def wechat():
#     if request.method == 'GET':
#         token = 'uroot666'
#         data = request.args
#         signature = data.get('signature','')
#         timestamp = data.get('timestamp','')
#         nonce = data.get('nonce','')
#         echostr = data.get('echostr','')
#         s = [timestamp, nonce, token]
#         s.sort()
#         s = bytes(''.join(s), encoding='utf8')
#         print(hashlib.sha1(s).hexdigest())
#     if hashlib.sha1(s).hexdigest() == signature:
#         return echostr
#     else:
#         return ''
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/static/')
def index_static():
    return render_template('index.html')

@app.route('/weixin/book/', methods=['GET','POST'])
def get_book():
    if request.method == 'GET':
        barcode = request.args.get('barcode', '')
        data = model.book_information(barcode)
        # data = json.dumps(data)
        # return Response(data, mimetype='application/json')
    elif request.method == 'POST':
        pass
    return data
    
@app.route('/weixin/address/add/', methods=['GET','POST'])
def address_add():
    address = request.args.get('address', '')
    print(address)
    if address:
        model.add_address(address)
    return json.dumps({'code':200})

@app.route('/book/list/', methods=['GET', 'POST'])
def book_list():
    num = request.args.get('num', '')
    bookList = model.book_list(num)
    print(num)
    return json.dumps(bookList, ensure_ascii=False)

@app.errorhandler(404)
def page_not_fount(e):
    return json.dumps({'prompt':'error'}, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)