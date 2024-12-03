# FILEPATH: /cloudide/workspace/EncodeMe/EncodingMe/API/login_handler.py
import sys
sys.path.append(".")
from flask import jsonify, request
import psycopg2
from API.connDB import connect_to_db
# 登录接口
def _login(username , password):

    conn = connect_to_db()
    cur = conn.cursor()

    # 查询数据库以验证用户
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        # 用户存在，返回成功信息
        user_data = {
            'user_id': user[0],
            'username': user[1],
        }
        return jsonify({'message': 'Login successful', 'user': user_data}), 200
    else:
        # 用户不存在或密码错误，返回错误信息
        return jsonify({'message': 'Invalid credentials'}), 401