
from __future__ import print_function

import argparse

import grpc

import iris_pb2
import iris_pb2_grpc


def run(host, port):
    channel = grpc.insecure_channel('%s:%d' % (host, port))
    stub = iris_pb2_grpc.IrisPredictorStub(channel)
    request = iris_pb2.IrisPredictRequest(
        sepal_length=5.0,
        sepal_width=3.6,
        petal_length=1.3,
        petal_width=0.25
    )
    response = stub.PredictIrisSpecies(request)
    print("Predicted species number: " + str(response.species))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='host name', default='localhost', type=str)
    parser.add_argument('--port', help='port number', default=50052, type=int)

    args = parser.parse_args()
    run(args.host, args.port)
