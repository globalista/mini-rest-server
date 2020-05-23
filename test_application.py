from application import Application
from unittest.mock import Mock

def test_get():
    scripts = Mock()
    app = Application(scripts)
    app.get_users()
    scripts.get.assert_called_once()
    

def test_post():
    scripts = Mock()
    app = Application(scripts)
    app.add_user('some name')
    scripts.add.assert_called_once_with('some_name')


def test_delete():
    scripts = Mock()
    app = Application(scripts)
    app.delete_user('another some name')
    scripts.delete.assert_called_once_with('another some name')