from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Server works!"

@app.route('/users', methods=['GET'])
def get_users():
    completed_proc = subprocess.run('./scripts/list-ftp-account.sh')
    return str(completed_proc.stdout)

@app.route('/users', methods=['POST'])
def add_user():
    completed_proc = subprocess.run(['./scripts/add-ftp-account.sh', '<NEW_USER>', '<PASSWORD>'])
    return (completed_proc.returncode) 

@app.route('/users/<username>', methods=['DELETE'])
def delete_user():
    completed_proc = subprocess.run(['./scripts/del-ftp-account.sh', '<USERNAME>'])
    return (completed_proc.returncode)

if __name__ == '__main__':
    app.run(debug=True)