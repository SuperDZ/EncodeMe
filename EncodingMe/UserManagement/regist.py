# FILEPATH: /cloudide/workspace/EncodeMe/EncodingMe/UserManagement/regist.py
import sys
sys.path.append(".")
from flask import jsonify, request
import psycopg2
from API.connDB import connect_to_db
def _register(usr_id, usr_relname, usr_name, usr_password, usr_department, usr_phone):
    conn = connect_to_db()
    cur = conn.cursor()

    # 检查用户名是否已存在
    try:
        cur.execute("SELECT * FROM users WHERE usr_id = %s", (usr_id,))
        existing_user = cur.fetchone()
        if existing_user:
            cur.close()
            conn.close()
            return {"message": "工号已被使用", "code": 500}, 500
    except Exception as e:
        print("continue")

    # 插入新用户
    try:
        cur.execute("INSERT INTO users(usr_id, usr_name, usr_pwd) VALUES(%s, %s, %s)", (usr_id, usr_name, usr_password))
        cur.execute("INSERT INTO user_info(usr_id, relname, usr_department, usr_phone) VALUES(%s, %s, %s, %s)", (usr_id, usr_relname, usr_department, usr_phone))
        conn.commit()
        cur.close()
        conn.close()
        print("录入成功")
        return {"message": "successful", "user_id": usr_id, "user_name": usr_name,"code": 200}
    except Exception as e:
        print("录入失败, 事务回滚")
        conn.rollback()
        cur.close()
        conn.close()
        return {"message": '录入失败',"code": 500}