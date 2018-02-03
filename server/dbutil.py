#encoding=UTF-8
# 数据库函数

import pymysql
import traceback

config = {'host':"192.168.174.136", 
        "user":"root", 
        "password":"passwd", 
        "database":"test",
        "charset":"utf8"
}

def db_operating(sql, if_fach,args=()):
    try:
        rt_cnt, rt_list = 0, []
        db = pymysql.connect(**config)
        cursor = db.cursor()
        rt_cnt = cursor.execute(sql, args)
        if if_fach:
            rt_list = cursor.fetchall()
        else:
            db.commit()
    except BaseException as e:
        print('db error')
        print(traceback.format_exc())
        db.rollback()
    finally:
        cursor.close()
        db.close()
    return rt_cnt,rt_list