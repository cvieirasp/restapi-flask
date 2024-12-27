APP = flaskapi

lint:
	@flake8 . --exclude .venv

compose:
	@docker compose build
	@docker compose up