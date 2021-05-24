from dbserver.dbworker import DBWorker
from multipledispatch import dispatch

class AvtoManager :

    def __init__(self):
        self.dbw = DBWorker('avtomobiles')
        self.separator = ';'

    def __splitvalues__(self, values: str) -> list[str]:
        if not values:
            return []
        return values.split(self.separator)

    def __mergevalues__(self, values: list) -> str:
        if not values:
            return ''
        return self.separator.join(values)

    def addbyprice(self, price: int) -> None:
        if price <= 0:
            raise ValueError('price is under zero')
        return self.dbw.addbyparams({'price': price})

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
    def findbyprice(self, price: int) -> list[dict]:
        return self.dbw.findbyparams({'price': price})

    @dispatch(dict)
    def findbyprice(self, obj: dict) -> list[dict]:
        return self.findbyprice(obj['price'])

    @dispatch(int, int)
    def updateprice(self, id: int, price: int) -> None:
        if price <= 0:
            raise ValueError('price is under zero')
        self.dbw.updatebyparams({'id': id, 'price': price})

    @dispatch(dict, int)
    def updateprice(self, obj: dict, price: int) -> None:
        self.updateprice(obj['id'], price)

if __name__ == '__main__':
    AV = AvtoManager()
    #AV.addbyprice(2000)
    obj = AV.findbyid(1)
    print(obj)
    print(AV.findall())
    AV.updateprice(obj, 2200)
    obj = AV.findbyid(1)
    print(obj)
    print(AV.findall())