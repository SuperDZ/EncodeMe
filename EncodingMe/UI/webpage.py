from flask import Flask, render_template, request, jsonify, send_from_directory, redirect, url_for
import os

app = Flask(__name__, template_folder='../UI')

# 静态文件路径配置
app.static_folder = '../UI'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/regist.html')
def register():
    return render_template('regist.html')

@app.route('/login', methods=['POST'])
def handle_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # TODO: 处理登录逻辑
    return '', 200

@app.route('/regist', methods=['POST'])
def handle_register():
    data = request.get_json()
    # TODO: 处理注册逻辑
    return '', 200

@app.route('/captcha')
def captcha():
    # TODO: 生成验证码图片
    return '', 200

@app.route('/bgPic/<path:filename>')
def serve_background(filename):
    return send_from_directory('../UI/bgPic', filename)

if __name__ == '__main__':
    app.run(debug=True)