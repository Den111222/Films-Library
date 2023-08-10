FROM python:3.11
ENV PYTHONUNBUFFERED=1
#RUN pip install pipenv
#WORKDIR /code
ARG WORKDIR=/code
ARG USER=user
WORKDIR ${WORKDIR}
RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt
COPY --chown=${USER} -R ${WORKDIR}
RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt \
    pip install git+https://github.com/Den111222/django-recaptcha3-0.4.1.git \


#RUN mkdir /code

#COPY Pipfile* /code/
#RUN pipenv install --system --deploy --ignore-pipfile
#ADD celery_redis /code/