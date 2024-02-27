"""
!pip install dlt[bigquery]

"""

# Authenticate to Google BigQuery
# from google.colab import auth
# auth.authenticate_user()

import os
import dlt
import requests
import json

os.environ['GOOGLE_CLOUD_PROJECT'] = 'dlt-dev-external'

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
    destination='bigquery',
    dataset_name='dtc'
)

# Run the pipeline
load_info = pipeline.run(stream_download_jsonl(url), table_name="users")

print(load_info)

from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

query = """
    SELECT *
    FROM `dtc.users`
"""

query_job = client.query(query)  # Make an API request.

print("The query data:")
for row in query_job:
    # Row values can be accessed by field name or index.
    print(row)