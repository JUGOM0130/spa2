from fastapi import APIRouter
from pydantic import BaseModel
import datetime as dt               # 日付
import logging
from typing import Union, List
import MysqlConnector
import random
import string

router = APIRouter(
    prefix='/tori',
    tags=['tori']
)


@router.get("/getListOfName")
def getListOfName():
    sql = """
        SELECT `m_tori`.`tid`,
            `m_tori`.`tname1`
        FROM `a_system`.`m_tori`;
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
