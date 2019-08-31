#External imports
from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

#Import classes
from task_service.task import Task, TaskList


# Create an instance of Flask
app = Flask(__name__)
api = Api(app)

api.add_resource(Task,'/tasks/<int:identifier>')
api.add_resource(TaskList, '/tasks')