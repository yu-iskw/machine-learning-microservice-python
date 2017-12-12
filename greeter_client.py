"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import argparse

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run(host, port):
    channel = grpc.insecure_channel('%s:%d' % (host, port))
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='cool guy'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='host name',
                        default='localhost',
                        type=str)
    parser.add_argument('--port', help='port number',
                        default=50051,
                        type=int)
    args = parser.parse_args()
    run(args.host, args.port)
