FROM python:3.5-jessie

RUN pip install --upgrade pip

ENV RUNNING_IN_DOCKER=true

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x ./run.sh

CMD ./run.sh
