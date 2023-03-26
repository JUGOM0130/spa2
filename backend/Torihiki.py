from fastapi import APIRouter
from pydantic import BaseModel
import logging
from typing import Union
import MysqlConnector

router = APIRouter(
    prefix='/torihiki',
    tags=['torihiki']
)


class TorihikiRegistData(BaseModel):
    tname1: Union[str, None]
    tname2: Union[str, None]
    zipcd: Union[str, None]
    address1: Union[str, None]
    address2: Union[str, None]
    address3: Union[str, None]
    address4: Union[str, None]
    tel1: Union[str, None]


# 取引先一覧画面で使用
# コードの詳細情報登録画面で使用
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


@router.post("/regist")
def regist(data: TorihikiRegistData):
    # タイトルが既に登録されているか？
    sql = """
        INSERT INTO `a_system`.`m_tori`
        (`tname1`,
        `tname2`,
        `zipcd`,
        `address1`,
        `address2`,
        `address3`,
        `address4`,
        `tel1`)
        VALUES (%(tname1)s,%(tname2)s,%(zipcd)s,%(address1)s,%(address2)s,%(address3)s,%(address4)s,%(tel1)s);
    """
    mci = MysqlConnector.Connector()
    row: int = 0
    try:
        dictdata: dict = dict(data)
        # INSERT処理
        drow = mci.insert(sql, dictdata)
        return {"result": {"status": "OK", "message": f"{drow} RowInserted"}}
    except Exception as e:
        print("== insert Exception ==")
        print(f"Error Occurred: {e}")
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        mci.close()
