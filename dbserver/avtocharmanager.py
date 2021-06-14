from dbserver.dbworker import DBWorker
from dbserver.avtomanager import AvtoManager
from dbserver.charmanager import CharManager
from multipledispatch import dispatch

class AvtoCharManager :

    def __init__(self, dbw: DBWorker):
        self.dbw = dbw
        #self.dbw = DBWorker('avto_characteristics')
        self.table = 'avto_characteristics'
        #self.am = AvtoManager()
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
    def findbyavto(self, avto_id: int) -> list[dict]:
        return self.dbw.findbyparams({'avto': avto_id}, self.table)

    @dispatch(dict)
    def findbyavto(self, avto_obj: dict) -> list[dict]:
        return self.findbyavto(avto_obj['id'])

    @dispatch(int)
    def findbychar(self, char_id: int) -> list[dict]:
        return self.dbw.findbyparams({'char': char_id}, self.table)

    @dispatch(dict)
    def findbychar(self, char_obj: dict) -> list[dict]:
        return self.findbyavto(char_obj['id'])

    @dispatch(int, int)
    def findbyavtochar(self, avto_id: int, char_id: int) -> list[dict]:
        return self.dbw.findbyparams({'avto': avto_id,'char': char_id}, self.table)

    @dispatch(dict, dict)
    def findbyavtochar(self, avto_obj: dict, char_obj: dict) -> list[dict]:
        return self.findbyavto(avto_obj['id'], char_obj['id'])

    @dispatch(int, int)
    def addbyac(self, avto_id: int, char_id: int) -> None:
        return self.dbw.addbyparams({'avto': avto_id, 'char': char_id}, self.table)

    @dispatch(int, int, str)
    def add(self, avto_id: int, char_id: int, value: str) -> None:
        return self.dbw.addbyparams({'avto': avto_id, 'char': char_id, 'value': value}, self.table)

    @dispatch(dict, dict, str)
    def add(self, avto_obj: dict, char_obj: dict, value: str) -> None:
        return self.add(avto_obj['id'], char_obj['id'], value)

    @dispatch(int, str)
    def updatevalue(self, id: int, value: str) -> None:
        return self.dbw.updatebyparams({'id': id, 'value': value}, self.table)

    @dispatch(dict, str)
    def updatevalue(self, obj: dict, value: str) -> None:
        return self.updatevalue(obj['id'], value)

    @dispatch(int)
    def deletebyid(self, id: int) -> None:
        return self.dbw.deletebyparams({'id': id}, self.table)

    @dispatch(dict)
    def deletebyid(self, obj: dict) -> None:
        return self.deletebyid(obj['id'])

    @dispatch(int, int)
    def deletebyac(self, avto_id: int, char_id: int) -> None:
        return self.dbw.deletebyparams({'avto': avto_id, 'char': char_id}, self.table)

    def getlogs(self):
        '''data = self.findall()
        CM = CharManager()
        AV = AvtoManager()'''
        data = self.dbw.getall()
        #print(data)
        '''
        avtoids = [d['id'] for d in AV.findall()]
        chardata = CM.findall()
        charids = [d['id'] for d in chardata]'''
        logs = ''
        for d in data:
            for k in d.keys():
                if k in ['id', 'price']:
                    continue
                if not d.get(k):
                    logs += 'Автомобиль "{}" не имеет значения характеристики "{}".\n'.format(d['id'], k)
        if not logs:
            logs = 'Значения характеристк автомобилей: нет предупреждений.\n'
        else:
            logs = 'Значения характеристк автомобилей:\n'+logs
        logs += '\n'
        return logs

if __name__ == '__main__':
    dbw = DBWorker()
    ACM = AvtoCharManager(dbw)
    print(ACM.getlogs())
    """objs = ACM.findall()
    print(objs)
    dbw.closeCon()
    dbw.openCon()
    ACM.addbyac(1, 18)
    obj = ACM.findbyavtochar(1, 18)
    print(obj)
    ACM.deletebyac(1, 18)
    obj = ACM.findbyavtochar(1, 18)
    print(obj)"""
    pass
