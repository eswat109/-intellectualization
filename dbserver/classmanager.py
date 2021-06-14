from dbserver.dbworker import DBWorker
from multipledispatch import dispatch

class ClassManager :

    def __init__(self, dbw: DBWorker):
        self.dbw = dbw
        self.table = 'classes'

    def gettitles(self):
        return self.dbw.gettitles(self.table)

    def findall(self) -> list[dict]:
        return self.dbw.findall(self.table)

    @dispatch(int)
    def findbyid(self, id: int) -> dict:
        if self.dbw.findbyparams({'id': id}, self.table):
            return self.dbw.findbyparams({'id': id}, self.table)[0]
        return None

    @dispatch(dict)
    def findbyid(self, obj: dict) -> dict:
        return self.findbyid(obj['id'])
    
    @dispatch(int)
    def deletebyid(self, id: int) -> None:
        return self.dbw.deletebyparams({'id': id}, self.table)

    @dispatch(dict)
    def deletebyid(self, obj: dict) -> None:
        return self.deletebyid(obj['id'])

    def addbyname(self, name: str) -> None:
        if not name:
            raise ValueError('name is empty')
        if self.findbyname(name):
            return
        return self.dbw.addbyparams({'name': name}, self.table)

    @dispatch(str)
    def findbyname(self, name: str) -> list[dict]:
        return self.dbw.findbyparams({'name': name}, self.table)

    @dispatch(dict)
    def findbyname(self, obj: dict) -> list[dict]:
        return self.findbyname(obj['name'])

    @dispatch(int, str)
    def updatename(self, id: int, name: str) -> None:
        self.dbw.updatebyparams({'id': id, 'name': name}, self.table)

    @dispatch(dict, str)
    def updatename(self, obj: dict, name: str) -> None:
        self.updatename(obj['id'], name)

    @dispatch(str)
    def findbybordlow(self, bordlow: str) -> list[dict]:
        return self.dbw.findbyparams({'bordlow': bordlow}, self.table)

    @dispatch(dict)
    def findbybordlow(self, obj: dict) -> list[dict]:
        return self.findbybordlow(obj['bordlow'])


    def updatebordlow(self, id: int, bordlow: int) -> None:
        self.dbw.updatebyparams({'id': id, 'bordlow': bordlow}, self.table)

    '''@dispatch(dict, int)
    def updatebordlow(self, obj: dict, bordlow: int) -> None:
        self.updatebordlow(obj[id], bordlow)'''

    '''@dispatch(str)
    def findbybordhigh(self, bordhigh: str) -> list[dict]:
        return self.dbw.findbyparams({'bordhigh': bordhigh}, self.table)'''

    '''@dispatch(dict)
    def findbybordhigh(self, obj: dict) -> list[dict]:
        return self.findbybordhigh(obj['bordhigh'])'''


    def updatebordhigh(self, id: int, bordhigh: int) -> None:
        self.dbw.updatebyparams({'id': id, 'bordhigh': bordhigh}, self.table)

    '''@dispatch(dict, int)
    def updatebordhigh(self, obj: dict, bordhigh: int) -> None:
        self.updatebordhigh(obj[id], bordhigh)'''

    def getlogs(self) -> str:
        data = self.findall()
        logs = 'Классы: \n'
        for d in data:
            if not d.get('bordlow'):
                logs += 'Класс "{}" не имеет нижней границы.\n'.format(d['name'])
            if not d.get('bordhigh'):
                logs += 'Класс "{}" не имеет верхней границы.\n'.format(d['name'])
        if logs == 'Классы: \n':
            logs += 'Нет предупреждений.\n'
        logs += '\n'
        return logs

if __name__ == '__main__':
    dbw = DBWorker()
    CM = ClassManager(dbw)
    res = CM.getlogs()
    print(res)

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
