FROM python:3.10.16-alpine3.21

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY application application
COPY main.py .

CMD ["python", "main.py"]