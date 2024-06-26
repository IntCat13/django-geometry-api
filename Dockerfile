FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "--bind", ":8000", "geo_api.wsgi:application"]