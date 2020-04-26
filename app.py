from flask import Flask, request, Response
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Server works!"

@app.route('/users', methods=['GET'])
def get_users():
    completed_proc = subprocess.run('./scripts/list-ftp-account.sh', stdout=subprocess.PIPE)
    if completed_proc.returncode == 0:
        return Response(completed_proc.stdout)
    return Response(status=500) 
    
@app.route('/users', methods=['POST'])
def add_user():
    print(request.form['name'])
    completed_proc = subprocess.run(['./scripts/add-ftp-account.sh', request.form['name']])
    if completed_proc.returncode == 0:
        return Response(status=200) 
    if completed_proc.returncode == 8:
        return Response(status=409)
    

@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    completed_proc = subprocess.run(['./scripts/del-ftp-account.sh', username])
    if completed_proc.returncode == 0:
        return Response(status=200)
    if completed_proc.returncode == 8:
        return Response(status=404)

if __name__ == '__main__':
    app.run(debug=True)