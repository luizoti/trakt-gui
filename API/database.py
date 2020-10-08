import sqlite3
from sqlite3 import Error

class DataBase():
    def __init__(self):
        self.db_file = join(dirname(dirname(realpath(sys.argv[0]))), 'database.db')

    def create_connection(self):
        try:
            _db = sqlite3.connect(self.db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

        _db.close()
        pass

        
db = DataBase()
db.create_connection()
# /home/luiz/trakt-gui-project/trakt-gui/API/database.db        