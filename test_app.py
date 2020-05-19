from app import app
import glob, subprocess

app.testing = True

def test_app():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Server works!'

def test_get():
    response = app.test_client().get('/users')

    assert response.status_code == 200
    data = response.data.decode('utf-8').strip().split('\n')
    assert len(data) == len(glob.glob('./data/*'))

def test_post():
    response = app.test_client().post('/users', data=dict(name="testtest"))
    assert response.status_code == 200
    response = app.test_client().post('/users', data=dict(name="testtest"))
    assert response.status_code == 409
    response = app.test_client().post('/users', data=dict(name="testtesttest"))
            

def test_delete():
    response = app.test_client().delete('/users/testtest')
    assert response.status_code == 200
    response = app.test_client().delete('/users/testtest')
    assert response.status_code == 404