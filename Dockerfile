FROM python:3.10

WORKDIR /app

COPY . .

ENV temp_value="Hello, I'm Docker"

CMD ["python", "main.py"]