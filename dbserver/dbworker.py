import sqlite3
from sqlite3 import Row

class DBWorker:

    def __init__(self, dbpath: str='D:\PythonProj\SII\dbserver\\testdb.db'):
        self.dbpath = dbpath
        #self.tablename = tablename
        self.openCon()

    def __del__(self):
        self.closeCon()

    def openCon(self):
        try:
            self.conn.close()
        except Exception:
            pass
        self.conn = sqlite3.connect(self.dbpath, timeout=10)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def closeCon(self):
        self.conn.close()

    """def printall(self):
        for row in self.cursor.execute("SELECT * FROM {} ".format(self.tablename)):
            print(dict(row))"""

    def gettitles(self, tables) -> list[str]:
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM {} ".format(tables))
        titles = self.cursor.description
        self.cursor.close()
        return [tuple[0] for tuple in titles]

    def gettitleswoclose(self, tables) -> list[str]:
        self.cursor.execute("SELECT * FROM {} ".format(tables))
        titles = self.cursor.description
        return [tuple[0] for tuple in titles]

    """def findall(self) -> list[dict]:
        self.cursor.execute("SELECT * FROM {} ".format(self.tablename))
        #return self.cursor.fetchall()
        res = self.cursor.fetchall()
        return [dict(t) for t in res]"""

    def findall(self, tables: str) -> list[dict]:
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM {} ".format(tables))
        #return self.cursor.fetchall()
        res = self.cursor.fetchall()
        self.cursor.close()
        return [dict(t) for t in res]

    """def findbyparams(self, params: dict) -> list[dict]:
        strvalues = "("
        for colname in self.gettitles():
            if params.get(colname):
                strvalues += colname + '= :' + colname + ' AND '
        strvalues += " 1=1)"
        req = "SELECT * FROM {} WHERE {}".format(self.tablename, strvalues)
        self.cursor.execute(req, params)
        #return self.cursor.fetchall()
        res = self.cursor.fetchall()
        return [dict(t) for t in res]"""

    def findbyparams(self, params: dict, tables: str) -> list[dict]:
        self.cursor = self.conn.cursor()
        strvalues = "("
        for colname in self.gettitleswoclose(tables):
            if params.get(colname):
                strvalues += colname + '= :' + colname + ' AND '
        strvalues += " 1=1)"
        req = "SELECT * FROM {} WHERE {}".format(tables, strvalues)
        self.cursor.execute(req, params)
        #return self.cursor.fetchall()
        res = self.cursor.fetchall()
        self.cursor.close()
        return [dict(t) for t in res]

    """def deletebyparams(self, params: dict) -> None:
        strvalues = ""
        for colname in self.gettitles():
            if params.get(colname):
                strvalues += colname + '= :' + colname + ' '
        strvalues = "("
        for colname in self.gettitles():
            if params.get(colname):
                strvalues += colname + '= :' + colname + ' AND '
        strvalues += " 1=1)"
        self.cursor.execute("DELETE FROM {} WHERE {}".format(self.tablename, strvalues), params)
        self.conn.commit()"""

    def deletebyparams(self, params: dict, tables: str) -> None:
        self.cursor = self.conn.cursor()
        """strvalues = ""
        for colname in self.gettitles():
            if params.get(colname):
                strvalues += colname + '= :' + colname + ' '"""
        strvalues = "("
        for colname in self.gettitleswoclose(tables):
            if params.get(colname):
                strvalues += colname + '= :' + colname + ' AND '
        strvalues += " 1=1)"
        self.cursor.execute("DELETE FROM {} WHERE {}".format(tables, strvalues), params)
        self.conn.commit()
        self.cursor.close()

    """def updatebyparams(self, params: dict) -> None:
        strvalues = ""
        for colname in self.gettitles()[1:]:
            if params.get(colname) != None:
                if params.get(colname) == '':
                    params[colname] = None
                if strvalues != "":
                    strvalues += ', '
                strvalues += colname + '= :' + colname
        key = self.gettitles()[0]
        strkey = key + '= :' + key
        req = "UPDATE {} SET {} WHERE {}".format(self.tablename, strvalues, strkey)
        self.cursor.execute(req, params)
        self.conn.commit()"""

    def updatebyparams(self, params: dict, tables: str) -> None:
        self.cursor = self.conn.cursor()
        strvalues = ""
        for colname in self.gettitleswoclose(tables)[1:]:
            if params.get(colname) != None:
                if params.get(colname) in ('', -1):
                    params[colname] = None
                if strvalues != "":
                    strvalues += ', '
                strvalues += colname + '= :' + colname
        key = self.gettitleswoclose(tables)[0]
        strkey = key + '= :' + key
        req = "UPDATE {} SET {} WHERE {}".format(tables, strvalues, strkey)
        self.cursor.execute(req, params)
        self.conn.commit()
        self.cursor.close()

    """def addbyparams(self, params: dict) -> None:
        strvalues = ""
        strcols = ""
        for colname in self.gettitles():
            if params.get(colname):
                if strvalues != "":
                    strvalues += ', '
                    strcols += ', '
                strvalues += ':' + colname
                strcols += colname
        req = "INSERT INTO {} ({}) VALUES ({})".format(self.tablename, strcols, strvalues)
        self.cursor.execute(req, params)
        self.conn.commit()"""

    def addbyparams(self, params: dict, tables: str) -> None:
        self.cursor = self.conn.cursor()
        strvalues = ""
        strcols = ""
        for colname in self.gettitleswoclose(tables):
            if params.get(colname):
                if strvalues != "":
                    strvalues += ', '
                    strcols += ', '
                strvalues += ':' + colname
                strcols += colname
        req = "INSERT INTO {} ({}) VALUES ({})".format(tables, strcols, strvalues)
        self.cursor.execute(req, params)
        self.conn.commit()
        self.cursor.close()


    """def addobj(self, obj: tuple) -> None:
        if len(obj) != len(self.gettitles()):
            raise ValueError('object and table haven\'t same length')
        strvalues = "(?"+ ",?"*(len(self.gettitles())-1) +")"
        self.cursor.execute("INSERT INTO {} VALUES {}".format(self.tablename, strvalues), obj)
        self.conn.commit()"""

    def findallfromall(self) -> list[dict]:
        self.cursor = self.conn.cursor()
        self.cursor.execute("select a.id, a.price, c.name, ac.value  from avtomobiles a \
            join avto_characteristics ac on ac.avto = a.id \
            join characteristics c on c.id = ac.char \
            order by a.id")
        #return self.cursor.fetchall()
        res = self.cursor.fetchall()
        self.cursor.close()
        return [dict(t) for t in res]

    def getall(self):
        dbw = DBWorker()
        res = dbw.findallfromall()
        #print(res)
        tmp_id = -1
        tmp_dict = {}
        allres = []
        for r in res:
            cur_id = r['id']
            if cur_id != tmp_id :
                if tmp_id != -1:
                    allres.append(tmp_dict)
                    tmp_dict = {}
                tmp_id = cur_id
                tmp_dict['id'] = r['id']
                tmp_dict['price'] = r['price']
            if not tmp_dict.get(r['name']):
                tmp_dict[r['name']] = r['value']
            else:
                tmp_dict[r['name']] = tmp_dict[r['name']]+';'+ r['value']
        allres.append(tmp_dict)
        #print(allres)
        return allres

    def pricechars(self, data: list[dict]) -> dict[dict[tuple]]:
        res = {}
        for d in data:
            curprice = d['price']
            tempdict = {}
            if not res.get(curprice):
                tempdict = {}
            else:
                tempdict = res[curprice]
            for k in d.keys():
                if k in ['id', 'price']:
                    continue
                value = None
                if not d[k]:
                    value = 'None'
                else:
                    value = d[k]
                if not tempdict.get(k):
                    tempdict[k] = [value,]
                else:
                    tempdict[k].append(value)
            res[curprice] = tempdict
        #print(res)
        return res

    def getprices(self, obj: dict, data: dict[dict[tuple]]) -> list:
        res = []
        for k in obj.keys():
            if not obj[k]:
                obj[k] = 'None'
        for price in data:
            pdict = data[price]
            flag = True
            for k in pdict.keys():
                if not obj.get(k):
                    continue
                n = obj[k]
                nn = pdict[k]
                if not (n in nn) and n != 'None':
                    flag = False
            if flag:
                res.append(price)
        return res

if __name__ == '__main__':
    dbw = DBWorker()
    res = dbw.getprices({'Название': 'Toyota Corolla', 'Год покупки': '1999', 'Тип двигателя': None}, dbw.pricechars(dbw.getall()))
    print(res)
    """

    d = {'id': 1, 'val': None, 'sas': ''}
    a = (d.get('id'))
    b = (d.get('sas'))
    c = (d.get('val'))
    print()
    """