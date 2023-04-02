import CONST
import mysql.connector as mycon
from typing import List


class Connector:

    def __init__(self) -> None:
        try:
            self.con = mycon.connect(
                user=CONST.CONST['user'],  # ユーザー名
                password=CONST.CONST['pw'],  # パスワード
                host=CONST.CONST['host'],  # ホスト名(IPアドレス）
                port=CONST.CONST['port'],
                auth_plugin='mysql_native_password'
            )
            self.con.ping(reconnect=True)  # 接続切れたときに再接続するか
            self.con.autocommit = False

            self.cur = self.con.cursor(dictionary=True)  # データを辞書型で取得する

            # print(self.con.is_connected())
        except Exception as e:
            print(e)
            self.con.close()
            self.cur.close()

    def get_cursor(self):
        return self.cur

    def insert(self, sql: str, value: tuple) -> int:
        rowcnt = 0
        try:
            cursor = self.cur
            cursor.execute(sql, value)
            rowcnt = cursor.rowcount
            self.con.commit()
        except Exception as e:
            print(e)

        return rowcnt

    def multiInsert(self, sql: str, value: List) -> int:
        rowcnt = 0
        try:
            cursor = self.cur
            cursor.executemany(sql, value)
            rowcnt = cursor.rowcount
            self.con.commit()
        except Exception as e:
            print("== multiInsertExcept ==\n\t== raiseします ==")
            raise e

        return rowcnt

    def delete(self, sql, value) -> int:
        rowcnt = 0
        try:
            cur = self.cur
            cur.execute(sql, value)
            rowcnt = cur.rowcount
            self.con.commit()
            print("削除しました")
        except Exception as e:
            print("== delete ==\n\t== raiseします ==")
            raise e
        return rowcnt

    def close(self) -> None:
        # cur閉じる
        self.cur.close()
        self.con.close()

    def getQuery(self, path):
        query: str
        with open(path, 'r', encoding='utf-8') as f:
            query = f.read()
        return query
