.PHONY: pytest

start:
	sudo docker compose -f docker-compose.yaml up

stop:
	sudo docker compose -f docker-compose.yaml stop

test-build:
	sudo docker compose -f docker-compose.dev.yaml up --detach

pytest:
	pytest -s

down:
	sudo docker compose -f docker-compose.dev.yaml down

test:
	$(MAKE) test-build
	$(MAKE) pytest || true
	$(MAKE) down
