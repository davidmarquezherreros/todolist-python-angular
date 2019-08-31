from constant_service import ConstantService, DatabaseService
from task_service import app



if __name__ == '__main__':
    DatabaseService.createStructure()
    if (ConstantService._createMockData == True):
        DatabaseService.insertMockData()

app.run(host=ConstantService._host, port=ConstantService._port, debug=True)