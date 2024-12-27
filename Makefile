APP = flaskapi

lint:
	@flake8 . --exclude .venv

test:
	@pytest -v --disable-warnings

compose:
	@docker compose build
	@docker compose up