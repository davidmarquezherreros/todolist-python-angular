#External imports
import sqlite3
from sqlite3 import Error

class ConstantService:
    _host = '0.0.0.0'
    _port = 80
    _databaseLocation = "application_database.sqlite"
    _createTaskTable = "CREATE TABLE IF NOT EXISTS tasks(ID INT, NAME VARCHAR(255), STATUS VARCHAR(255), DATE_START DATETIME, DATE_END DATETIME, PRIMARY KEY(`ID`));"
    _createMockData = False

class DatabaseService:
    @staticmethod
    def createStructure():
        conn = None
        try:
            
            conn = sqlite3.connect(ConstantService._databaseLocation)
            c = conn.cursor()
            c.execute(ConstantService._createTaskTable)
            
            return c.description

        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
    @staticmethod
    def insertMockData():
        conn = None
        try:

            conn = sqlite3.connect(ConstantService._databaseLocation)
            c = conn.cursor()

            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(0, 'TASK_NAME_0','PENDING','31-12-2019','31-12-2019');")
            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(1, 'TASK_NAME_1','PENDING','31-12-2019','31-12-2019');")
            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(2, 'TASK_NAME_2','PENDING','31-12-2019','31-12-2019');")
            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(3, 'TASK_NAME_3','PENDING','31-12-2019','31-12-2019');")
            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(4, 'TASK_NAME_4','PENDING','31-12-2019','31-12-2019');")
            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(5, 'TASK_NAME_5','PENDING','31-12-2019','31-12-2019');")
            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(6, 'TASK_NAME_6','PENDING','31-12-2019','31-12-2019');")
            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(7, 'TASK_NAME_7','PENDING','31-12-2019','31-12-2019');")
            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(8, 'TASK_NAME_8','PENDING','31-12-2019','31-12-2019');")
            c.execute("INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES(9, 'TASK_NAME_9','PENDING','31-12-2019','31-12-2019');")

            conn.commit()

            return sqlite3.sqlite_version
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    # Retrieves a task based on an ID
    @staticmethod
    def retrieveTask(id):
        conn = None
        try:

            conn = sqlite3.connect(ConstantService._databaseLocation)
            c = conn.cursor()
            command = "SELECT * FROM TASKS WHERE ID=" + str(id)
            c.execute(command)
            row = c.fetchone()

            return row

        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def retrieveAllTasks():
        conn = None
        try:

            conn = sqlite3.connect(ConstantService._databaseLocation)
            c = conn.cursor()
            command = "SELECT * FROM TASKS;"
            c.execute(command)
            rows = c.fetchall()
            
            return rows

        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
    
    @staticmethod
    def insertTask(id, name, status, date_start, date_end):
        conn = None
        try:

            conn = sqlite3.connect(ConstantService._databaseLocation)
            c = conn.cursor()

            commandSql = "INSERT INTO tasks(ID, NAME, STATUS, DATE_START, DATE_END) VALUES("
            commandSql += str(id) + ","
            commandSql += "'" + name + "',"
            commandSql += "'" + status + "',"
            commandSql += "'" + date_start + "',"
            commandSql += "'" + date_end + "');"
            c.execute(commandSql)
            conn.commit()

            return c.lastrowid

        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def updateTask(id, name, status, date_start, date_end):
        conn = None
        try:

            conn = sqlite3.connect(ConstantService._databaseLocation)
            c = conn.cursor()

            commandSql = "UPDATE TASKS SET"
            commandSql += " NAME ='" + name + "',"
            commandSql += "STATUS ='" + status + "',"
            commandSql += "DATE_START ='" + date_start + "',"
            commandSql += "DATE_END ='" + date_end + "'"
            commandSql += " WHERE ID =" + str(id) + ";"
            c.execute(commandSql)
            conn.commit()
            return 1

        except Error as e:
            print(e)
            return -1
        finally:
            if conn:
                conn.close()

    @staticmethod
    def deleteTask(id):
        conn = None
        try:

            conn = sqlite3.connect(ConstantService._databaseLocation)
            c = conn.cursor()
            commandSql = "DELETE FROM TASKS WHERE ID ="+ str(id) + ";"
            c.execute(commandSql)
            conn.commit()
            return c.rowcount

        except Error as e:
            print(e)
            return -1
        finally:
            if conn:
                conn.close()
