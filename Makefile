APP = flaskapi

lint:
	@flake8 . --exclude .venv

test:
	@pytest -v --disable-warnings

compose:
	@docker compose build
	@docker compose up

heroku:
	@heroku container:login
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web