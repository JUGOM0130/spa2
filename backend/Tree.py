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
    composition_id: str


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


@router.post('/regist')
def tree_regist(datas: List[TreeRegistData]):

    # ランダムな文字列生成
    randlst = [random.choice(string.ascii_letters + string.digits)
               for i in range(20)]
    random_str = ''.join(randlst)

    values = []
    for data in datas:
        values.append([str(random_str),
                       int(data.composition_id),
                       int(data.parts_id),
                       int(data.lv),
                       str(data.parent_id),
                       int(data.order)])
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
