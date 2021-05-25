from dbserver.dbworker import DBWorker
from multipledispatch import dispatch

class CharManager :

    def __init__(self):
        self.dbw = DBWorker('characteristics')
        self.types = {'int': 'int', 'log': 'log', 'enum': 'enum'}
        self.separator = ';'

    def __splitvalues__(self, values: str) -> list[str]:
        if not values:
            return []
        res = values.split(self.separator)
        if '' in res:
            res.remove('')
        return res

    def __mergevalues__(self, values: list) -> str:
        if not values:
            return ''
        return self.separator.join(values)

    def gettitles(self):
        return self.dbw.gettitles()

    """def add(self, name: str, type: str=None, values: tuple[str]=None) -> None:
        if not self.dbw.findbyparams({'name': name}) :
            return
        strvalues = ''
        if values:
            strvalues = self.separator.join(values)
        self.dbw.addobj((None, name, type, strvalues))"""

    def addbyname(self, name: str) -> None:
        if not name:
            raise ValueError('name is empty')
        if self.findbyname(name):
            return
        return self.dbw.addbyparams({'name': name})

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
    def deletebyid(self, id: int) -> None:
        return self.dbw.deletebyparams({'id': id})

    @dispatch(dict)
    def deletebyid(self, obj: dict) -> None:
        return self.deletebyid(obj['id'])

    @dispatch(str)
    def findbyname(self, name: str) -> list[dict]:
        return self.dbw.findbyparams({'name': name})

    @dispatch(dict)
    def findbyname(self, obj: dict) -> list[dict]:
        return self.findbyname(obj['name'])

    @dispatch(str)
    def findbytype(self, type: str) -> list[dict]:
        return self.dbw.findbyparams({'type': type})

    @dispatch(dict)
    def findbytype(self, obj: dict) -> list[dict]:
        return self.findbytype(obj['type'])

    @dispatch(int, str)
    def updatename(self, id: int, name: str) -> None:
        self.dbw.updatebyparams({'id': id, 'name': name})

    @dispatch(dict, str)
    def updatename(self, obj: dict, name: str) -> None:
        self.updatename(obj['id'], name)

    @dispatch(int, str)
    def updatetype(self, id: int, type: str) -> None:
        self.dbw.updatebyparams({'id': id, 'type': type, 'cvalues': ""})

    @dispatch(dict, str)
    def updatetype(self, obj: dict, type: str) -> None:
        self.updatetype(obj[id], type)

    """@dispatch(dict, str)
    def updatetype(self, obj: dict, type: str) -> dict:
        self.updatetype(obj[id], type)
        if self.findbyid(obj[id]):
            return self.findbyid(obj[id])[0]
        return {}"""

    @dispatch(int, str)
    def addvalue(self, id: int, value: str) -> None:
        if not value:
            return
        obj = self.findbyid(id)
        if not obj :
            return
        values = self.__splitvalues__(obj['cvalues'])
        if value in values:
            return
        values.append(value)
        self.dbw.updatebyparams({'id': id, 'cvalues': self.__mergevalues__(values)})

    @dispatch(dict, str)
    def addvalue(self, obj: dict, value: str) -> None:
        return self.addvalue(obj['id'], value)

    @dispatch(int, str)
    def removevalue(self, id: int, value: str) -> None:
        obj = self.findbyid(id)
        if not obj :
            return
        values = self.__splitvalues__(obj['cvalues'])
        if value in values:
            values.remove(value)
        self.dbw.updatebyparams({'id': id, 'cvalues': self.__mergevalues__(values)})

    @dispatch(dict, str)
    def removevalue(self, obj: dict, value: str) -> None:
        return self.removevalue(obj['id'], value)

    @dispatch(int, str, str)
    def updatevalue(self, id: int, oldv: str, newv: str) -> None:
        self.removevalue(id, oldv)
        self.addvalue(id, newv)

    @dispatch(dict, str, str)
    def updatevalue(self, obj: dict, oldv: str, newv: str) -> None:
        self.removevalue(obj, oldv)
        self.addvalue(obj, newv)

    @dispatch(int)
    def deletevalue(self, id: int) -> None:
        obj = self.findbyid(id)
        if not obj:
            return
        self.dbw.updatebyparams({'id': id, 'cvalues': ''})

    @dispatch(dict)
    def deletevalue(self, obj: dict) -> None:
        return self.deletevalue(obj['id'])


if __name__ == '__main__':
    CM = CharManager()

    """obj = CM.findbyid(7)
    print(obj)
    CM.addvalue(obj, 'false')
    obj = CM.findbyid(obj)
    print(obj)
    CM.addvalue(obj, '')
    obj = CM.findbyid(obj)
    print(obj)
    CM.deletevalue(obj)
    obj = CM.findbyid(obj)
    print(obj)"""
    """CM.addvalue(obj, '')
    obj = CM.findbyid(obj)
    print(obj)
    CM.addvalue(obj, '')
    obj = CM.findbyid(obj)
    print(obj)"""
    """CM.updatevalue(obj, 'true', 'TRUE')
    obj = CM.findbyid(obj)
    print(obj)
    CM.removevalue(obj, 'TRUE')
    obj = CM.findbyid(obj)
    print(obj)"""
