FROM python:3.9.6-alpine3.14

ENV PYTHONBUFFERED 1
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  # Pillow Dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext 

COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
ENV DJANGO_SECRET_KEY='c419364d9d9e179554782ec06359644b7587400678f1324873f8a72d66320e4e41315f417feae960113cc86df5aaae93753dc3c66ebc504d70b9974540caffec'

WORKDIR /app

