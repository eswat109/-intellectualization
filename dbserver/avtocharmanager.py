from dbserver.dbworker import DBWorker
from dbserver.avtomanager import AvtoManager
from dbserver.charmanager import CharManager
from multipledispatch import dispatch

class AvtoCharManager :

    def __init__(self):
        self.dbw = DBWorker('avto_characteristic')
        self.am = AvtoManager()
        self.separator = ';'

    def __splitvalues__(self, values: str) -> list[str]:
        if not values:
            return []
        return values.split(self.separator)

    def __mergevalues__(self, values: list) -> str:
        if not values:
            return ''
        return self.separator.join(values)

    def findall(self) -> list[dict]:
        return self.dbw.findall()

    @dispatch(int)
    def findbyid(self, id: int) -> dict:
        if self.dbw.findbyparams({'id': id}):
            return self.dbw.findbyparams({'id': id})[0]
        return None

    @dispatch(dict)
    def findbyid(self, obj: dict) -> dict:
        return self.findbyid(obj['id'])

    @dispatch(int)
    def findbyavto(self, avto_id: int) -> list[dict]:
        return self.dbw.findbyparams({'avto': avto_id})

    @dispatch(dict)
    def findbyavto(self, avto_obj: dict) -> list[dict]:
        return self.findbyavto(avto_obj['id'])

    @dispatch(int)
    def findbychar(self, char_id: int) -> list[dict]:
        return self.dbw.findbyparams({'char': char_id})

    @dispatch(dict)
    def findbychar(self, char_obj: dict) -> list[dict]:
        return self.findbyavto(char_obj['id'])

    @dispatch(int, int)
    def findbyavtochar(self, avto_id: int, char_id: int) -> list[dict]:
        return self.dbw.findbyparams({'avto': avto_id,'char': char_id})

    @dispatch(dict, dict)
    def findbyavtochar(self, avto_obj: dict, char_obj: dict) -> list[dict]:
        return self.findbyavto(avto_obj['id'], char_obj['id'])

    @dispatch(int, int, str)
    def add(self, avto_id: int, char_id: int, value: str) -> None:
        return self.dbw.addbyparams({'avto': avto_id, 'char': char_id, 'value': value})

    @dispatch(dict, dict, str)
    def add(self, avto_obj: dict, char_obj: dict, value: str) -> None:
        return self.add(avto_obj['id'], char_obj['id'], value)

    @dispatch(int, str)
    def updatevalue(self, id: int, value: str) -> None:
        return self.dbw.updatebyparams({'id': id, 'value': value})

    @dispatch(dict, str)
    def updatevalue(self, obj: dict, value: str) -> None:
        return self.updatevalue(obj['id'], value)

    @dispatch(int)
    def deletebyid(self, id: int) -> None:
        return self.dbw.deletebyparams({'id': id})

    @dispatch(dict)
    def deletebyid(self, obj: dict) -> None:
        return self.deletebyid(obj['id'])

if __name__ == '__main__':

    pass
