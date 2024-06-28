FROM python:3.12.4-slim

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

WORKDIR /app
COPY . /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]