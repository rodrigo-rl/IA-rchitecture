FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ADD ./ /API

WORKDIR /API

RUN pip install -r requirements.txt

ENV PORT=8080

CMD uvicorn main:app --host 0.0.0.0 --port=${PORT}