FROM python:3.10.12-slim-bullseye

WORKDIR /clock-api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py" , "--mode", "container"]

#commando docker build --tag clock-api .
#commando docker run -d -p 5000:5000 clock-api
