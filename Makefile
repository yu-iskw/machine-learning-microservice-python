NAME := iris-predictor
PYTHON_VERSION := 3.6

build-docker:
	docker build . -t $(NAME)

run-docker:
	docker run --rm -d -p 50052:50052 --name $(NAME) $(NAME)

create-conda:
	conda env create -f environment.yml -n $(NAME)

delete-conda:
	conda env remove -y -n $(NAME)
