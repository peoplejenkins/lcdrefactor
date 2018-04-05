FROM python:3.6.5-alpine3.7

WORKDIR /usr/src/app

COPY Data.py Data.py
COPY Digit.py Digit.py
COPY main.py main.py

CMD [ "python", "main.py" ]

