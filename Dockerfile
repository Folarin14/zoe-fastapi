# 
FROM python:3.9.13-slim-buster

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./zoe /app/zoe

EXPOSE 8000

CMD ["uvicorn", "zoe.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--reload"]
