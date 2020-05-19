from flask import Flask, request
from application import Application
from scripts import Scripts

#app = Flask(__name__)

my_scripts = Scripts()
app = Application(my_scripts)
    

@app.route('/')
def index():
    return "Server works!"

@app.route('/users', methods=['GET'])
def get_users():
    return app.get_users()

@app.route('/users', methods=['POST'])
def add_user():
    return app.add_user(request.form['name'])


@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    return app.delete_user(username)
    
if __name__ == '__main__':
    app.run(debug=True)