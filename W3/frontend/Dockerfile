FROM python:3.11.9-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app

EXPOSE 3000

CMD ["python", "app.py"]