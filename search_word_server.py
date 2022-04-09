"""
在线查单词服务端
"""
from multiprocessing import process
from socket import *
from pymysql import *

class SearchWordTCP:
    pass

class SearchWordSQL:
    def __init__(self):
        self.kwargs = {
            "host":'localhost',
            "port":3306,
            "user":'root',
            "password":'123456',
            "database":'dict',
            "charset":'utf8'
        }
        self.db = connect(**self.kwargs)
        self.cur = self.db.cursor()

    def test(self):
        sql = 'select * from words limit 10;'
        self.cur.execute(sql)
        for item in self.cur:
            print(item)

class SearchWordHandle:
    pass

class SearchWordProcess(process):
    pass


if __name__ == '__main__':
    s = SearchWordSQL()
    s.test()