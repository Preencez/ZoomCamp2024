FROM python:3.9.1

# Install system dependencies
RUN apt-get update && apt-get install -y wget

# Install Python dependencies with retry and increased timeout
RUN pip install --timeout 600 --index-url https://pypi.python.org/simple/ --trusted-host pypi.python.org pandas sqlalchemy psycopg2 pyarrow

# Set the working directory
WORKDIR /app

# Copy the application files
COPY ingest_data.py ingest_data.py

# Set the entry point
ENTRYPOINT ["python", "ingest_data.py"]

# Set default command (can be overridden when running the container)
CMD ["--user", "root", "--password", "root", "--host", "localhost", "--port", "5432", "--db", "ny_taxi", "--table_name", "green_taxi_data", "--csv_path", "C:\Project Folder\ZoomCamp2024\week_1 docker\green_tripdata_2019.csv"]
