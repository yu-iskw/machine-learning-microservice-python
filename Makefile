CONDA_NAME := machine-learning-microservice-python
PYTHON_VERSION := 3.6

DOCKER_TAG := python-grpc-example

build-docker:
	docker build . -t $(DOCKER_TAG)

run-docker:
	docker run --rm -d -p 50052:50052 --name grpc-example $(DOCKER_TAG)

create-conda:
	conda env create -f environment.yml -n $(CONDA_NAME)

delete-conda:
	conda env remove -y -n $(CONDA_NAME)
