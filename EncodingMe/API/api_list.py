import sys
sys.path.append(".")
from flask import Flask, request, jsonify
import psycopg2
from connDB import connect_to_db
from UserManagement.login import _login
from UserManagement.regist import _register

app = Flask(__name__)

# 假设您已经有一个用户模型
class User:
    def __init__(self, userid, username, password):
        self.user_id = userid
        self.username = username
        self.password = password

# 登录接口
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    result = _login(username, password)
    return jsonify({'result': result}), 200

# 注册接口
@app.route('/register', methods=['POST'])
def regist():
    data = request.get_json()
    usr_id = data['usr_id']
    usr_relname = data['relname']   #relname是真实姓名
    usr_name = data['username']     #username是用户名
    usr_password = data['password']
    usr_department = data['department']
    usr_phone = data['phone']
    result, status_code = _register(usr_id, usr_relname, usr_name, usr_password, usr_department, usr_phone)
    return result, status_code

# 信息修改接口
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    new_username = data['username']
    new_email = data['email']

    conn = connect_to_db()
    cur = conn.cursor()

    # 更新用户信息
    cur.execute("UPDATE users SET username = %s, email = %s WHERE user_id = %s", (new_username, new_email, user_id))
    conn.commit()

    cur.close()
    conn.close()

    # 返回成功信息
    return jsonify({'message': 'User information updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
