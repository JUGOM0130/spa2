from fastapi import APIRouter
from pydantic import BaseModel
import datetime as dt               # 日付
import logging
from typing import Union
import MysqlConnector
router = APIRouter(
    prefix='/tree',
    tags=['tree']
)


class TreeRegistData(BaseModel):
    tree_id: int
    composition_id: int
    parts_id: int


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


@router.post('/tree_regist')
def tree_regist(td: TreeRegistData):
    reg_sql = """
    INSERT INTO `a_system`.`t_tree_table`
    (`tree_id`,
    `composition_id`,
    `parts_id`)
    VALUES
    (%s,%s,%s);
    """
    values = (td.tree_id,
              td.composition_id,
              td.parts_id,)
    mci = MysqlConnector.Connector()
    row: int = 0
    try:
        # INSERT処理
        row = mci.insert(reg_sql, values)
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        mci.close()
        return {"result": {"status": "OK", "message": f"{row} RowInsert"}}
