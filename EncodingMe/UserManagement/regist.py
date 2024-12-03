# FILEPATH: /cloudide/workspace/EncodeMe/EncodingMe/UserManagement/regist.py
from flask import jsonify, request
import psycopg2
from EncodingMe.API.connDB import connect_to_db
def _register(usr_id, usr_relname, usr_name, usr_password, usr_department, usr_phone):
    conn = connect_to_db()
    cur = conn.cursor()

    # 检查用户名是否已存在
    cur.execute("SELECT * FROM users WHERE usr_id = %s", (usr_id,))
    existing_user = cur.fetchone()

    if existing_user:
        cur.close()
        conn.close()
        return jsonify({'message': '工号已被使用'}), 400

    # 插入新用户
    cur.execute("INSERT INTO users (id, username, password) VALUES (%s, %s, %s) RETURNING user_id", (usr_id, usr_name, usr_password))
    cur.execute("INSERT INTO user_info (id, relname, department, phone) VALUES (%s, %s, %s, %s)", (usr_id, usr_relname, usr_department, usr_phone))
    user_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    # 返回成功信息和新用户的ID
    return jsonify({'message': 'Registration successful', 'user_id': user_id, 'user_name': usr_name}), 200