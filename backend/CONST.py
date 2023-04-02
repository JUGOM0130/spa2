import sys
import logging

# デフォルト設定
logging.basicConfig(level=logging.DEBUG)
CONST = {
    'user': 'admin',
    'pw': '0000',
    'host': 'localhost',
    'db': 'a_system',
    'port': '3306'
}

if len(sys.argv) > 1:
    # 本番環境用設定
    if sys.argv[1] == "PRO":
        print("本番環境運用")
        # ログレベル設定 リリース時はINFO以上に設定する
        logging.basicConfig(level=logging.DEBUG)

        # 定数設定
        CONST = {
            'user': 'admin',
            'pw': '0000',
            'host': '192.168.0.20',
            'db': 'a_system',
            'port': '3306'
        }
    # 会社Windows
    elif sys.argv[1] == "WIN":
        print("Win環境運用")
        # ログレベル設定 リリース時はINFO以上に設定する
        logging.basicConfig(level=logging.DEBUG)

        # 定数設定
        CONST = {
            'user': 'root',
            'pw': '0000000000',
            'host': 'localhost',
            'db': 'a_system',
            'port': '3306'
        }
    elif sys.argv[1] == "AVAIL":
        print("AVAIL環境運用")
        # ログレベル設定 リリース時はINFO以上に設定する
        logging.basicConfig(level=logging.DEBUG)

        # 定数設定
        CONST = {
            'user': 'root',
            'pw': '0000000000',
            'host': 'localhost',
            'db': 'a_system',
            'port': '3306'
        }
    # 検証環境用
    else:
        print("検証環境運用")
        # ログレベル設定 リリース時はINFO以上に設定する
        logging.basicConfig(level=logging.DEBUG)

        # 定数設定
        CONST = {
            'user': 'admin',
            'pw': '0000',
            'host': 'localhost',
            'db': 'a_system',
            'port': '3306'
        }
else:
    print("引数なし検証環境運用")
    # ログレベル設定 リリース時はINFO以上に設定する
    logging.basicConfig(level=logging.DEBUG)

    # 定数設定
    CONST = {
        'user': 'admin',
        'pw': '0000',
        'host': 'localhost',
        'db': 'a_system',
        'port': '3306'
    }
