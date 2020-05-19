import subprocess

class Scripts:

    def get(self):
        return subprocess.run('./scripts/list-ftp-account.sh', stdout=subprocess.PIPE)
    
    def add(self, new_user):
        return subprocess.run(['./scripts/add-ftp-account.sh', new_user, './data/'])
    
    def delete(self, user):
        return subprocess.run(['./scripts/del-ftp-account.sh', user, './data/'])
