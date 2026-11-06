.RECIPEPREFIX = >

install:
>uv sync

lint:
>uv run ruff check .

test-coverage:
>uv run pytest --cov=gendiff --cov-report=term --cov-report=xml
