import pandas as pd
import pyarrow.parquet as pq

# Some fancy job with pandas

#print("Job finished successfully")





# Read Parquet file into an Arrow Table
yellow_tripdata_2021= pq.read_table("C:\Project Folder\ZoomCamp2024\yellow_tripdata_2021-01.parquet")

# Convert Arrow Table to Pandas DataFrame
yellow_tripdata_2021 = yellow_tripdata_2021.to_pandas()

# Save Pandas DataFrame to CSV file
yellow_tripdata_2021.to_csv('yellow_tripdata_2021.csv', index=False)


# Read Parquet file into an Arrow Table
green_tripdata_2019= pq.read_table("C:\Project Folder\ZoomCamp2024\green_tripdata_2019-01.parquet")

# Convert Arrow Table to Pandas DataFrame
green_tripdata_2019 = green_tripdata_2019.to_pandas()

# Save Pandas DataFrame to CSV file
green_tripdata_2019.to_csv('green_tripdata_2019.csv', index=False)
