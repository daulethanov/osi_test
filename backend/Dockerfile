FROM python:3.10.7

RUN pip install pipenv
WORKDIR /OSI

COPY Pipfile Pipfile.lock ./

RUN pipenv install --dev --system --deploy

COPY . .

CMD gunicorn --bind 0.0.0.0:5000 runserver:app

