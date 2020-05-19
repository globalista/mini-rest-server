from flask import Flask, Response

class Application(Flask):

    def __init__(self, scripts):
        super().__init__(__name__)
        self.scripts = scripts

    def get_users(self):
        completed_proc = self.scripts.get()
        if completed_proc.returncode == 0:
            return Response(completed_proc.stdout)

    def add_user(self, user):
        completed_proc = self.scripts.add(user)
        if completed_proc.returncode == 0:
            return Response(status=200) 
        if completed_proc.returncode == 8:
            return Response(status=409)

    def delete_user(self, user):
        completed_proc = self.scripts.delete(user)
        if completed_proc.returncode == 0:
            return Response(status=200)
        if completed_proc.returncode == 8:
            return Response(status=404)
    