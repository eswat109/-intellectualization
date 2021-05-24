from dbserver.dbworker import DBWorker
from multipledispatch import dispatch

class AvtoCharManager :

    def __init__(self):
        self.dbw = DBWorker('avto_characteristic')
        self.separator = ';'

    def __splitvalues__(self, values: str) -> list[str]:
        if not values:
            return []
        return values.split(self.separator)

    def __mergevalues__(self, values: list) -> str:
        if not values:
            return ''
        return self.separator.join(values)

    def addbyprice(self, price: str) -> None:
        return self.dbw.addbyparams({'price': price})

    def findall(self) -> list[dict]:
        return self.dbw.findall()

    def findbyid(self, id: int) -> list[dict]:
        return self.dbw.findbyparams({'id': id})

    def findbyprice(self, price: str) -> list[dict]:
        return self.dbw.findbyparams({'price': price})

    def updateprice(self, id: int, price: str) -> None:
        self.dbw.updatebyparams({'id': id, 'price': price})