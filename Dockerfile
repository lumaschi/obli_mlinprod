FROM python:3.9.12

WORKDIR /scrapers
COPY . .
RUN pip install -r requirements.txt
RUN pip install azure-storage-blob

CMD scrapy crawl gallito