import mysql.connector
class StudentDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datarepresentation"
 )

    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from student"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.converttoDictionary(result))
        return results

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from student where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.converttoDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update student set name= %s, age=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from student where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")
    
    def converttoDictionary(self, result):
        colnames=['id', 'Artist', 'Title', 'Label', 'Price']
        item = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item 

studentDAO = StudentDAO()