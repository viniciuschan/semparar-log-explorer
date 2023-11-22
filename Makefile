install:
	poetry install

lint:
	poetry run isort . && poetry run black .

test:
	poetry run pytest -sx

run:
	python -m app.main
