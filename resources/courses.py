
from flask import jsonify, Blueprint
from flask.ext.restful import Resource, Api, reqparse, inputs

import models


class CourseList( Resource ):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No course title Provided',
            location=['form', 'json']       # Counterintuitively, last is first
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No course URL provided',
            location=['form', 'json'],
            type=inputs.url              # allows valid URLs to be detected. Cool.
        )
        super(self.__class__, self).__init__()                   # Makes sure that standard setup still happens
                                                                 # Note that super().__init__() was not valid,
                                                                 # and this is because you are using python 2

    def get( self ):
        return jsonify({'courses': [{'title': 'Python Basics'}]})

    def post(self):
        args = self.reqparse.parse_args()      # parses arguments as specified in init
        models.Course.create( **args)          # Creates instance in database of the arguments (if not intercepted
                                               # by line above
        return jsonify({'courses': [{'title': 'Python Basics'}]})


class Course(Resource):
    def get(self, id):
        return jsonify({'title': 'Python Basics'})

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})


courses_api = Blueprint('resources.courses', __name__)
api = Api(courses_api)
api.add_resource(
    CourseList,
    '/api/v1/courses',
    endpoint='courses'
)
api.add_resource(
    Course,
    '/api/v1/courses/<int:id>',
    endpoint='course'
)
