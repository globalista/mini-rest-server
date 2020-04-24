from flask import Flask, json, make_response, request, Response
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Server works!"

@app.route('/users', methods=['GET'])
def get_users():
    completed_proc = subprocess.run('./scripts/list-ftp-account.sh', stdout=subprocess.PIPE)
    if completed_proc.returncode == 0:
        #rv = make_response(Response(completed_proc.stdout))
        #return rv
        #return Response(completed_proc.stdout)
        return make_response(completed_proc.stdout)
    print('Oops...')
    return None 
    
@app.route('/users', methods=['POST'])
def add_user():
    print(request.form['name'])
    completed_proc = subprocess.run(['./scripts/add-ftp-account.sh', request.form['name']])
    if completed_proc.returncode == 0:
        return Response(status=200) 
    if completed_proc.returncode == 8:
        return '409'
    

@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    completed_proc = subprocess.run(['./scripts/del-ftp-account.sh', username])
    if completed_proc.returncode == 0:
        return Response(status=200).status
    if completed_proc.returncode == 8:
        return '404'

if __name__ == '__main__':
    app.run(debug=True)