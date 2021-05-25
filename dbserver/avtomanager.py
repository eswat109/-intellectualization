from dbserver.dbworker import DBWorker
from multipledispatch import dispatch

class AvtoManager :

    def __init__(self, dbw: DBWorker):
        self.dbw = dbw
        #self.dbw = DBWorker('avtomobiles')
        self.table = 'avtomobiles'
        self.separator = ';'

    def __splitvalues__(self, values: str) -> list[str]:
        if not values:
            return []
        return values.split(self.separator)

    def __mergevalues__(self, values: list) -> str:
        if not values:
            return ''
        return self.separator.join(values)

    def gettitles(self):
        return self.dbw.gettitles(self.table)

    def addbyidprice(self, id: int, price: int) -> None:
        if price <= 0 or id <= 0:
            raise ValueError('price is under zero')
        return self.dbw.addbyparams({'id': id,'price': price}, self.table)

    def addbyprice(self, price: int) -> None:
        if price <= 0:
            raise ValueError('price is under zero')
        return self.dbw.addbyparams({'price': price}, self.table)

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

    @dispatch(int)
    def findbyprice(self, price: int) -> list[dict]:
        return self.dbw.findbyparams({'price': price}, self.table)

    @dispatch(dict)
    def findbyprice(self, obj: dict) -> list[dict]:
        return self.findbyprice(obj['price'])

    @dispatch(int, int)
    def updateprice(self, id: int, price: int) -> None:
        if price <= 0:
            raise ValueError('price is under zero')
        self.dbw.updatebyparams({'id': id, 'price': price}, self.table)

    @dispatch(dict, int)
    def updateprice(self, obj: dict, price: int) -> None:
        self.updateprice(obj['id'], price)

if __name__ == '__main__':
    dbw = DBWorker()
    AV = AvtoManager(dbw)
    #AV.addbyprice(2000)
    AV.addbyidprice(4, 1000)
    obj = AV.findbyid(4)
    print(obj)
    """print(AV.findall())
    AV.updateprice(obj, 2200)
    obj = AV.findbyid(1)
    print(obj)
    print(AV.findall())"""