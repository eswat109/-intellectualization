import sqlite3
from sqlite3 import Row

class DBWorker:

    def __init__(self, tablename: str, dbpath: str='D:\PythonProj\SII\dbserver\\testdb.db'):
        self.dbpath = dbpath
        self.tablename = tablename
        try:
            self.conn = sqlite3.connect(self.dbpath, timeout=10)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
        except sqlite3.DatabaseError as e:
            print(e)

    def __del__(self):
        self.conn.close()

    def printall(self):
        for row in self.cursor.execute("SELECT * FROM {} ".format(self.tablename)):
            print(dict(row))

    def gettitles(self) -> list[str]:
        self.cursor.execute("SELECT * FROM {} ".format(self.tablename))
        return [tuple[0] for tuple in self.cursor.description]

    def findall(self) -> list[dict]:
        self.cursor.execute("SELECT * FROM {} ".format(self.tablename))
        #return self.cursor.fetchall()
        res = self.cursor.fetchall()
        return [dict(t) for t in res]

    """def findbyid(self, id: int)-> list[dict]:
        if id < 0:
            raise ValueError('id is under zero')
        self.cursor.execute("SELECT * FROM {} WHERE id = :id ORDER BY id".format(self.tablename), {'id': id})
        #return self.cursor.fetchall()
        res = self.cursor.fetchall()
        return [dict(t) for t in res]"""

    def findbyparams(self, params: dict) -> list[dict]:
        strvalues = "("
        for colname in self.gettitles():
            if params.get(colname):
                strvalues += colname + '= :' + colname + ' AND '
        strvalues += " 1=1)"
        req = "SELECT * FROM {} WHERE {}".format(self.tablename, strvalues)
        self.cursor.execute(req, params)
        #return self.cursor.fetchall()
        res = self.cursor.fetchall()
        return [dict(t) for t in res]

    def deletebyparams(self, params: dict) -> None:
        strvalues = ""
        for colname in self.gettitles():
            if params.get(colname):
                strvalues += colname + '= :' + colname + ' '
        self.cursor.execute("DELETE FROM {} WHERE {}".format(self.tablename, strvalues), params)
        self.conn.commit()

    def updatebyparams(self, params: dict) -> None:
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
        self.conn.commit()

    def addbyparams(self, params: dict) -> None:
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
        self.conn.commit()

    def addobj(self, obj: tuple) -> None:
        if len(obj) != len(self.gettitles()):
            raise ValueError('object and table haven\'t same length')
        strvalues = "(?"+ ",?"*(len(self.gettitles())-1) +")"
        """if name in self.getcharacteristicsnames():
            raise ValueError('already exist characteristic: {}'.format(name))"""
        self.cursor.execute("INSERT INTO {} VALUES {}".format(self.tablename, strvalues), obj)
        self.conn.commit()




if __name__ == '__main__':
    dbw = DBWorker('characteristics')
    #dbw.addobj((None, 'e6', 'log', None))
    #dbw.addbyparams({'name': 'asddf'})
    #dbw.deletebyparams({'id': 15})
    #dbw.updatebyparams({'id': 7, 'type': 'e'})

    dbw.updatebyparams({'id': 7, 'cvalues': ''})
    #dbw.printall()
    res = dbw.findall()
    print(res)
    """

    d = {'id': 1, 'val': None, 'sas': ''}
    a = (d.get('id'))
    b = (d.get('sas'))
    c = (d.get('val'))
    print()
    """