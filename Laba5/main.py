import sqlite3

class AskSql:
    arg = None
    def __init__(self, nameDb = "myDB.db"):
        self.connection = sqlite3.connect(nameDb)
    #use onece with each name
    def createDB(self, name = "person", arg = ("name", "age", "job", "social_status", "musical_genre")):
        self.name = name
        self.count = 0
        string = "("
        for i in arg:
            string += i + " text, "
            self.count += 1
        string = string[:-2]
        string += ")"
        print(string)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE " + name + " " + string)
    def add(self, value = ("Nikita", "19", "BMXer", "Bichugan", "Metalcore")):
        count = 0
        string = "("
        for i in value:
            string += i + " text, "
            count += 1
        string = string[:-2]
        string += ")"
        print(string)
        if count > self.count:
            tmp = "?," * (count/self.count)
            self.cursor.executemany("INSERT INTO " + self.name + " VALUES ( " + tmp + " )", value)
        else:
            self.cursor.execute("INSERT INTO " + self.name + " " + string)
        self.connection.commit()
    
    def update(self,sorce, replacement, position):
        sql = "UPDATE " + self.name + " SET " + position + " = \'" + replacement + "\' WHERE " + position + " = \'" + sorce + "\'"
        self.cursor.execute(sql)
        self.connection.commit()

def main():
    db = AskSql()
    db.createDB()
    value = [] 
    db.add(value)
    value = []
main()