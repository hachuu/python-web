from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import logging

app = Flask(__name__)

# 로그 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.info(f'hi')

app.secret_key = 'any random string'

# 가상으로 사용자 정보를 저장하는 딕셔너리
users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
    'shy': '1234'
}

def is_logged_in():
    return 'username' in session

@app.route('/login', methods=['GET'])
def login():
    app.logger.debug("Rendering login.html")  # 로그 출력 예시
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def loginPost():
    if request.method == 'POST':
        logger.info(f"Processing login request {request}")
        logger.info(f"Processing login request {request.json}")


        if request.json:
            username = request.json.get('username')
            password = request.json.get('password')

            # 사용자가 입력한 정보와 딕셔너리에 저장된 정보를 비교하여 로그인 여부 확인
            if username in users and users[username] == password:
                session['username'] = username
                # return redirect(url_for('main'))
                return jsonify({"status": "success"})
            else:
                app.logger.warning(f"Login failed for user {username}.")
                return jsonify({"status": "error", "message": "Invalid username or password"}), 401
        else:
            app.logger.warning(f"Login failed for user {username}.")
            return jsonify({"status": "error", "message": "Invalid username or password"}), 401

    return render_template('login.html')

@app.route('/main')
def main():
    if not is_logged_in():
        return redirect(url_for('login'))

    # log 
    username = session['username']
    app.logger.info(f"User '{username}' logged in successfully.")
    return render_template('main.html', username=username)

@app.route('/apple')
def apple():
    return render_template('apple.html')

if __name__ == '__main__':
    app.run(debug=True)
    # 소스를 고칠 때마다 자동 시작
