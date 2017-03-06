
from flask import jsonify
from flask.ext.restful import Resource

import models


class ReviewList(Resource):
    def getSelf(self):
        return jsonify({'reviews': [{'course': 1, 'Rating': 5}]})


class Review(Resource):
    def get(self, id):
        return jsonify({'course': 1, 'Rating': 5})

    def put(self, id):
        return jsonify({'course': 1, 'Rating': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'Rating': 5})

