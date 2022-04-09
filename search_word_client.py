"""
在线查单词客户端
"""
from socket import *

class SearchWordView:
    def __init__(self):
        self.__controller = SearchWordController()


    def __menu1(self):
        print("""
        ╔===============在线字典=================╗
        |                                        |
        |   --------------首页------------       |
        |   1. 登陆                              |
        |   2. 注册                              |
        |   3. 退出                              |
        |   ------------------------------       |
        |   说明：通过数字键选择菜单             |
        ╚========================================╝
        """)
    def __menu2(self):
        print("""
        ╔===============在线字典=================╗
        |                                        |
        |   -------------查单词------------      |
        |   1. 查单词                            |
        |   2. 历史记录                          |
        |   3. 注销                              |
        |   ------------------------------       |
        |   说明：通过数字键选择菜单             |
        ╚========================================╝
        """)

    def __select_menu(self):
        self.__menu1()
        option = input('请输入选项：')
        if option == '1':
            self.__controller.login()
        elif option == '2':
            self.__controller.register()
        elif option == '3':
            exit()


class SearchWordController:
    def __init__(self):
        self.__sock = SearchWordTCP().connect_server()


class SearchWordTCP:
    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = '8888'
        self.__address = (self.__host, self.__port)
        self.__sock = socket()

    def connect_server(self):
        self.__sock.connect(self.__address)
        return self.__sock
