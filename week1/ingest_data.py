import os
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine

def main(args):
    user = args.user
    password = args.password
    host = args.host
    port = args.port
    db = args.db
    table_name = args.table_name
    csv_path = args.csv_path

    # Create a SQLAlchemy engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Read CSV file in chunks
    df_iter = pd.read_csv(os.path.abspath(csv_path), iterator=True, chunksize=100000)

    # Specify the output file path for the CSV in the desired directory
    output_directory = "/app/output_folder/"
    os.makedirs(output_directory, exist_ok=True)

    # Concatenate the output directory and the CSV file name
    output_csv_path = os.path.join(output_directory, "output.csv")

    # Write the first chunk to the database
    df = next(df_iter)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')

    # Save the first chunk to a CSV file
    df.to_csv(output_csv_path, index=False)
    print(f"Saved CSV file to: {output_csv_path}")


    while True:
        try:
            # Read the next chunk
            t_start = time()
            df = next(df_iter)
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

            # Append the chunk to the database
            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()
            print('Inserted another chunk, took %.3f seconds' % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the PostgreSQL database")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to PostgreSQL')

    parser.add_argument('--user', required=True, help='user name for PostgreSQL')
    parser.add_argument('--password', required=True, help='password for PostgreSQL')
    parser.add_argument('--host', required=True, help='host for PostgreSQL')
    parser.add_argument('--port', required=True, help='port for PostgreSQL')
    parser.add_argument('--db', required=True, help='database name for PostgreSQL')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('csv_path', help='file path of the CSV file')

    args = parser.parse_args()
    main(args)
