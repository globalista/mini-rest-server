from application import Application
from scripts import Scripts
from unittest.mock import Mock

def test_get1():
    # testing if application is calling the right script
    scripts = Mock()
    app = Application(scripts)
    app.get_users()
    scripts.get.assert_called_once()
    
def test_get2():
    # testing response
    scripts = Mock()
    app = Application(scripts)
    scripts.get().returncode = 0
    assert app.get_users().status_code == 200

def test_post1():
    scripts = Mock()
    app = Application(scripts)
    app.add_user('some name')
    scripts.add.assert_called_once_with('some name')

def test_post2():
    scripts = Mock()
    app = Application(scripts)
    scripts.add().returncode = 0
    assert app.add_user('etwas').status_code == 200
    scripts.add().returncode = 8
    assert app.add_user('etwas2').status_code == 409


def test_delete():
    scripts = Mock()
    app = Application(scripts)
    app.delete_user('another some name')
    scripts.delete.assert_called_once_with('another some name')

def test_delete2():
    scripts = Mock()
    app = Application(scripts)
    scripts.delete().returncode = 0
    assert app.delete_user('nekdo').status_code == 200
    scripts.delete().returncode = 8
    assert app.delete_user('nekdo jiny').status_code == 404