import logging

# ログレベル設定 リリース時はINFO以上に設定する
logging.basicConfig(level=logging.DEBUG)

# 定数設定 自宅用
'''
CONST = {
    'user': 'admin',
    'pw': '0000',
    'host': '192.168.0.20',
    'db': 'a_system'
}
'''
# C2248
CONST = {
    'user': 'root',
    'pw': '0000000000',
    'host': '127.0.0.1',
    'db': 'a_system'
}