"""
%%capture
!pip install dlt[parquet] # Install dlt with all the necessary DuckDB dependencies
!pip install parquet
!mkdir .dlt
"""

import os
import dlt
# import parquet
import json
import glob
import requests

# Set the bucket_url. We can also use a local folder
os.environ['DESTINATION__FILESYSTEM__BUCKET_URL'] = 'file:///content/.dlt/my_folder'

url = "https://storage.googleapis.com/dtc_zoomcamp_api/yellow_tripdata_2009-06.jsonl"

def stream_download_jsonl(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    for line in response.iter_lines():
        if line:
            yield json.loads(line)

# Define your pipeline
pipeline = dlt.pipeline(
    pipeline_name='my_pipeline',
    destination='filesystem',
    dataset_name='mydata'
)



# Run the pipeline with the generator we created earlier.
load_info = pipeline.run(stream_download_jsonl(url), table_name="users", loader_file_format="parquet")

print(load_info)

# Get a list of all Parquet files in the specified folder
parquet_files = glob.glob('/content/.dlt/my_folder/mydata/users/*.parquet')

# show parquet files
print("Loaded files: ")
for file in parquet_files:
  print(file)