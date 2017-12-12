# gRPC example in python

This is an example to run gRPC server on docker as well as access the server from a client on a local machine.
Those files in the repository derives from an official example.

- [grpc/examples/python/helloworld at master · grpc/grpc](https://github.com/grpc/grpc/tree/master/examples/python/helloworld)

## Requirements

- Docker
- Anaconda
- Make

## Implement the files

1. Define the protocol-buffer in `helloworld.proto`.
2. Implement a command to generate python files from `helloworld.proto` in `codegen.py`.
3. Implement `grpc_server.py`.
4. Implement `greeter_server.py`.

## How to set up an environment on our local machine
The command creates an anaconda environment.
We can activate the environment with `source activate grpc-example`, since the environment name is `grpc-example`.
```
make create-conda

# If you would like to remove the anaconda envronment,
make delete-conda
```

## How to run the server and the client on our local machine
```
python grpc_server.py

python greeter_client.py
Greeter client received: Hello, cool guy!
```

## How to build and run a docker image
The docker image is used for running `grpc_server.py`.
The host name depends on your environment.
If you use `docker-machine`, we can see the IP address with `docker-machine ip YOUR_DOCKER_MACHINE`.
```
make build-docker

make run-docker
```

And then, we check if the client can access the server on docker or not:

```
# Execute it on your local machine, not a docker container.
python greeter_cliept.py --host HOST_NAME --port 50051
```
