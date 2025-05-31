run:
	docker build -t scavengers_reader .
	docker run -it --rm --name scavengers_reader --env-file=.env scavengers_reader
