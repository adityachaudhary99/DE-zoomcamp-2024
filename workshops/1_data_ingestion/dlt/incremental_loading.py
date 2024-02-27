import dlt
import duckdb

data = [
    {
        "vendor_name": "VTS",
				"record_hash": "b00361a396177a9cb410ff61f20015ad",
        "time": {
            "pickup": "2009-06-14 23:23:00",
            "dropoff": "2009-06-14 23:48:00"
        },
        "Trip_Distance": 17.52,
        "coordinates": {
            "start": {
                "lon": -73.787442,
                "lat": 40.641525
            },
            "end": {
                "lon": -73.980072,
                "lat": 40.742963
            }
        },
        "Rate_Code": None,
        "store_and_forward": None,
        "Payment": {
            "type": "Credit",
            "amt": 20.5,
            "surcharge": 0,
            "mta_tax": None,
            "tip": 9,
            "tolls": 4.15,
						"status": "cancelled"
        },
        "Passenger_Count": 2,
        "passengers": [
            {"name": "John", "rating": 4.4},
            {"name": "Jack", "rating": 3.6}
        ],
        "Stops": [
            {"lon": -73.6, "lat": 40.6},
            {"lon": -73.5, "lat": 40.5}
        ]
    },
]

# define the connection to load to.
# We now use duckdb, but you can switch to Bigquery later
pipeline = dlt.pipeline(pipeline_name='taxi_data_load', destination='duckdb', dataset_name='taxi_rides')

# run the pipeline with default settings, and capture the outcome
info = pipeline.run(data,
										table_name="rides",
										write_disposition="merge",
                    primary_key='record_hash')

# show the outcome

conn = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")

# let's see the tables
conn.sql(f"SET search_path = '{pipeline.dataset_name}'")
print('Loaded tables: ')
print(conn.sql("show tables"))


print("\n\n\n Rides table below: Note the times are properly typed")
rides = conn.sql("SELECT * FROM rides").df()
print(rides)

print("\n\n\n Pasengers table")
passengers = conn.sql("SELECT * FROM rides__passengers").df()
print(passengers)
print("\n\n\n Stops table")
stops = conn.sql("SELECT * FROM rides__stops").df()
print(stops)
