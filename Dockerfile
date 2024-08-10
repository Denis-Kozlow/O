FROM python:3.12-slim

ENV POETRY_VERSION=0.1.0

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

WORKDIR /dep

COPY pyproject.toml poetry.lock* /dep/

RUN poetry install --no-root --no-interaction --no-ansi

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
