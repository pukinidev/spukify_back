FROM python:3.12-slim

WORKDIR /app

RUN pip3 install fastapi uvicorn pydantic sqlalchemy psycopg2-binary

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]