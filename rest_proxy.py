# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import grpc

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, fields, marshal

import iris_pb2
import iris_pb2_grpc

app = Flask(__name__)
api = Api(app)


class HealthCheck(Resource):
    """
    This class is used for health check.
    """
    def get(self):
        return {"status": "alive"}, 200


class RestProxy(Resource):
    """
    This class is used for a proxy with REST to a gRPC server.
    """

    # Define the inputs.
    parser = reqparse.RequestParser()
    parser.add_argument('sepal_length', type=float, help='sepal length', required=True)
    parser.add_argument('sepal_width', type=float, help='sepal width', required=True)
    parser.add_argument('petal_length', type=float, help='petal length', required=True)
    parser.add_argument('petal_width', type=float, help='petal width', required=True)
    parser.add_argument('threshold', type=float, help='threshold', required=False, default=0.5)

    # Define the outputs.
    resource_fields = {
        'species': fields.String,
    }

    def __init__(self, host, port):
        """
        :param host: host of gRPC server.
        :param port: port of gRPC server.
        """
        self.host = host
        self.port = port

    def post(self):
        # Parse arguments by REST request.
        args = self.__class__.parser.parse_args()

        # Request to the gRPC server.
        channel = grpc.insecure_channel('%s:%s' % (self.host, self.port))
        stub = iris_pb2_grpc.IrisPredictorStub(channel)
        request = iris_pb2.IrisPredictRequest(
            sepal_length=args['sepal_length'],
            sepal_width=args['sepal_width'],
            petal_length=args['petal_length'],
            petal_width=args['petal_width']
        )
        response = stub.PredictIrisSpecies(request)

        # Return the results.
        data = {
            'species': response.species,
        }
        return marshal(data, self.__class__.resource_fields)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='REST server host', default='localhost', type=str)
    parser.add_argument('--port', help='REST server port', default=5000, type=int)
    parser.add_argument('--grpc_host', help='gRPC server host', default='0.0.0.0', type=str)
    parser.add_argument('--grpc_port', help='gRPC server port', default=50052, type=int)
    parser.add_argument('--debug', help='debug flag', default=False, type=bool)
    args = parser.parse_args()

    resource_class_kwargs = {
        'host': args.grpc_host,
        'port': args.grpc_port,
    }

    # Run flask app
    api.add_resource(RestProxy, '/', resource_class_kwargs=resource_class_kwargs)
    api.add_resource(HealthCheck, '/healthcheck')
    app.run(host=args.host, port=args.port, debug=args.debug)
