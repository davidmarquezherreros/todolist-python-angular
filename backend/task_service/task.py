#External imports
from flask_restful import Resource, reqparse

#Import classes
from constant_service import DatabaseService

parser = reqparse.RequestParser()
parser.add_argument('name', help='Name of the task')
parser.add_argument('status', help='Status of the task')
parser.add_argument('date_start', help='Start date of the task')
parser.add_argument('date_end', help='End date of the task')

#Class model
class Task(Resource):
    def get(self, identifier):
        task = DatabaseService.retrieveTask(identifier)
        
        if (task is None):
            return {'message': 'Not found', 'data': [] }, 404
        else:
            
            return {'message': 'Success', 'data': [
                {
                    'id': task[0],
                    'name': task[1],
                    'status': task[2],
                    'date_start': task[3],
                    'date_end': task[4]
                }
            ] }, 200
    def post(self, identifier):
        try:
            args = parser.parse_args(strict=True)
        except:
            return {'message': 'Bad request', 'data': []}, 400

        if (args is None):
            return {'message': 'Internal Error', 'data': [] }, 500
        else:
            createdId = DatabaseService.insertTask(identifier, args['name'], args['status'], args['date_start'], args['date_end'])
            if (createdId is None):
                return {'message': 'Bad request', 'data': []}, 400
            else:
                return {
                    'message': 'Object created successfully', 'data': 
                    [
                        {
                            'id': createdId,
                            'name': args['name'],
                            'status': args['status'],
                            'date_start': args['date_start'],
                            'date_end': args['date_end']
                        }
                    ]
                }, 201
    def put(self, identifier):
        try:
            args = parser.parse_args(strict=True)
        except:
            return {'message': 'Bad request', 'data': []}, 400

        if (args is None):
            return {'message': 'Internal Error', 'data': [] }, 500
        else:
            updatedId = DatabaseService.updateTask(identifier, args['name'], args['status'], args['date_start'], args['date_end'])
            if (updatedId is None):
                return {'message': 'Bad request', 'data': []}, 400
            if (updatedId == -1):
                return {'message': 'Not found', 'data': []}, 404
            else:
                return {
                    'message': 'Object updated successfully', 'data': 
                    [
                        {
                            'id': identifier,
                            'name': args['name'],
                            'status': args['status'],
                            'date_start': args['date_start'],
                            'date_end': args['date_end']
                        }
                    ]
                }, 200

    def delete(self, identifier):
        deletedId = DatabaseService.deleteTask(identifier)
        
        if (deletedId is None):
            return {'message': 'Internal Error', 'data': [] }, 500
        if (deletedId == 0):
            return {'message': 'Not found', 'data': [] }, 404
        else:
            return {'message': 'Object deleted successfully', 'data': [] }, 200









class TaskList(Resource):
    def get(self):
        tasks = DatabaseService.retrieveAllTasks()

        result = []

        if (tasks is None):
            return {'message': 'Not found', 'data': [] }, 404
        else:
            for task in tasks:
                result.append({ 'id': task[0], 'name': task[1], 'status': task[2], 'date_start': task[3], 'date_end': task[4] })
            return {'message': 'Success', 'data': result }, 200
        