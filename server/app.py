#encoding: utf-8

from flask import Flask
from flask import request
from flask import Response

import hashlib
import requests
import json

import model

app = Flask(__name__)

@app.route('/')
def index():
    return 'dushu.atimo.cn'

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
    

@app.errorhandler(404)
def page_not_fount(e):
    return json.dumps({'prompt':'error'},ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)