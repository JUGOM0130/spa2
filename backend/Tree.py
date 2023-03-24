from fastapi import APIRouter
from pydantic import BaseModel
import datetime as dt               # 日付
import logging
from typing import Union, List
import MysqlConnector
import random
import string


router = APIRouter(
    prefix='/tree',
    tags=['tree']
)


class TreeRegistData(BaseModel):
    tree_id: Union[str, None]
    parts_id: str
    name: str
    lv: str
    parent_id: str
    order: str
    insu: int
    bosu: int
    composition_id: str


class TreeId(BaseModel):
    tree_id: str

# ルートノードになりうるものを取得


@router.get('/get_root_list')
def getRootList():
    sql = """
    SELECT
        `m_parts`.`pid`,
        `m_parts`.`pcd`,
        `m_parts`.`pname`
    FROM `a_system`.`m_parts`;
    """

    mci = MysqlConnector.Connector()
    try:
        cursor = mci.get_cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        rowcnt = cursor.rowcount

        logging.debug(data)

        return {"result": {"status": "OK", "message": f"{rowcnt} getDatas", "data": data}}
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        mci.close()


# ツリーの一覧取得
@router.get('/get_tree_list')
def getTreeList():
    sql = """
        SELECT tree_id
        FROM a_system.t_tree_table
        GROUP BY tree_id
    """

    mci = MysqlConnector.Connector()
    try:
        cursor = mci.get_cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        rowcnt = cursor.rowcount

        logging.debug(data)

        return {"result": {"status": "OK", "message": f"{rowcnt} getDatas", "data": data}}
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        mci.close()

# 登録


@router.post('/regist')
def tree_regist(datas: List[TreeRegistData]):

    # ランダムな文字列生成
    randlst = [random.choice(string.ascii_letters + string.digits)
               for i in range(20)]
    random_str = ''.join(randlst)

    # 登録処理を実行するかのフラグ
    exeflag = True

    # RootNodeをタイトルに設定
    title = ""
    for d in datas:
        if d.lv == "1":
            title = d.name

    # タイトルが既に登録されているか？
    chk_sql = """
        SELECT
            count(tree_id) as rowcnt
        FROM
            a_system.t_tree_table
        WHERE
            tree_id = %s;
    """
    mci = MysqlConnector.Connector()
    try:
        cur = mci.get_cursor()
        cur.execute(chk_sql, (title,))
        row = cur.fetchall()
        if row[0]['rowcnt'] > 0:
            exeflag = False
    except Exception as e:
        mci.close()
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}

    # RootNodeと同じものが登録されていなければ登録処理を行う
    # 以下登録処理
    if exeflag:
        values = []
        for data in datas:
            values.append([str(title),
                           int(data.composition_id),
                           int(data.parts_id),
                           int(data.lv),
                           str(data.parent_id),
                           int(data.order),
                           int(data.insu),
                           int(data.bosu)])

        mci = MysqlConnector.Connector()
        reg_sql = mci.getQuery("./TreeQuerys/tree_regist.sql")
        row: int = 0
        try:
            # INSERT処理
            print(values)
            row = mci.multiInsert(reg_sql, values)
            return {"result": {"status": "OK", "message": f"{row} RowInsert"}}
        except Exception as e:
            print("== tree_regist Exception ==")
            print(f"Error Occurred: {e}")
            return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
        finally:
            mci.close()
    else:
        return {"result": {"status": "ERR", "message": "既に登録済みです。"}}


# 更新
@router.post('/update')
def tree_update(datas: List[TreeRegistData]):

    # タイトルが既に登録されているか？
    del_sql = """
        DELETE FROM `a_system`.`t_tree_table`
        WHERE tree_id = %(title)s;
    """

    # RootNodeをタイトルに設定
    title = ""
    for d in datas:
        if d.lv == "1":
            title = d.name

    # RootNodeと同じものが登録されていなければ登録処理を行う
    # 以下更新処理
    values = []
    for data in datas:
        values.append([str(title),
                       int(data.composition_id),
                       int(data.parts_id),
                       int(data.lv),
                       str(data.parent_id),
                       int(data.order),
                       int(data.insu),
                       int(data.bosu)])

    mci = MysqlConnector.Connector()
    row: int = 0
    try:
        # DELETE処理
        drow = mci.delete(del_sql, {'title': title})

        # INSERTクエリの取得
        reg_sql = mci.getQuery("./TreeQuerys/tree_regist.sql")

        # INSERT処理
        row = mci.multiInsert(reg_sql, values)
        return {"result": {"status": "OK", "message": f"{drow} RowDeleted {row} RowInserted"}}
    except Exception as e:
        print("== tree_regist Exception ==")
        print(f"Error Occurred: {e}")
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        mci.close()


# ツリーの一覧取得
@router.get('/delete/{tree_id}')
def delete(tree_id: str):
    # タイトルが既に登録されているか？
    del_sql = """
        DELETE FROM `a_system`.`t_tree_table`
        WHERE tree_id = %(title)s;
    """
    mci = MysqlConnector.Connector()
    row: int = 0
    try:
        # DELETE処理
        drow = mci.delete(del_sql, {'title': tree_id})
        return {"result": {"status": "OK", "message": f"{drow} RowDeleted"}}
    except Exception as e:
        print("== delete Exception ==")
        print(f"Error Occurred: {e}")
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        mci.close()


# ツリーの一覧取得
@router.post('/get_tree_datas')
def getTreeDatas(tree: TreeId):
    print(tree)
    sql = """
        SELECT `t_tree_table`.`tree_id`,
                `t_tree_table`.`composition_id`,
                `t_tree_table`.`parts_id`,
                `m_parts`.`pcd`,
                `t_tree_table`.`lv`,
                `t_tree_table`.`parent_id`,
                `t_tree_table`.`order`,
                `t_tree_table`.`insu`,
                `t_tree_table`.`bosu`
            FROM `a_system`.`t_tree_table`,`a_system`.`m_parts`
            WHERE `m_parts`.`pid` = `t_tree_table`.`parts_id`
            AND tree_id = %s;
        """

    mci = MysqlConnector.Connector()
    try:
        cursor = mci.get_cursor()
        cursor.execute(sql, (tree.tree_id,))
        data = cursor.fetchall()
        rowcnt = cursor.rowcount

        logging.debug(data)

        return {"result": {"status": "OK", "message": f"{rowcnt} getDatas", "data": data}}
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        mci.close()
