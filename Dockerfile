FROM python:3.7.4-slim-stretch as Python

COPY requirements.txt .

# install deps
RUN apt-get update --fix-missing
RUN pip install -r requirements.txt

# nodejs (optional)
# RUN apt-get update --fix-missing 
# RUN apt-get install curl -y --fix-missing
# RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && apt-get install -y nodejs npm && npm install --global yarn

FROM python:3.7.4-slim-stretch

COPY --from=Python /root/.cache /root/.cache
COPY --from=Python requirements.txt .

RUN apt-get update
RUN pip install -r requirements.txt 
RUN rm -rf /root/.cache 
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir app
WORKDIR /app

COPY ./ /app/

CMD python manage.py runserver 0.0.0.0:8000
