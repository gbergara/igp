TAG=igp:latest

build:
	docker build -t $(TAG) .

run:
	docker run -it $(TAG) /bin/bash

clean:
	docker rmi $(TAG)


