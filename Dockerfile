FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

EXPOSE 5001

CMD ["python3", "app.py"]
