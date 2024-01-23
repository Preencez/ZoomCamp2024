
# # This docker code is to contanarize Data ingestion process
FROM python:3.9.1

# RUN apt-get install wget 
# RUN pip install pandas sqlalchemy psycopg2
RUN apt-get update && \ 
    apt-get install -y wget && \
    rm -rf /var/lib/apt/lists/*
# This code works for me 

RUN pip install pandas sqlalchemy psycopg2 wget

WORKDIR /app
COPY ingest_data.py ingest_data.py 

ENTRYPOINT [ "python", "ingest_data.py" ]

