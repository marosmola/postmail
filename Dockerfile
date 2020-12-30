FROM python:3.8-alpine


RUN apk --no-cache add \
    build-base \
    postgresql-dev \
    bash \
    make

COPY requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app/

ENTRYPOINT ["make"]
CMD ["runserver"]
