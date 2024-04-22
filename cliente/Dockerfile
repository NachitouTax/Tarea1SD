FROM python:3.9-slim

COPY ./cliente /home/app

WORKDIR /home/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3.9", "-u", "client.py"]
