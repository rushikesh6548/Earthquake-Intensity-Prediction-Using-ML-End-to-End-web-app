import os
import logging
import pandas
from io import StringIO

import pandas as pd
import requests


def get_all_data_from_api():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    global earthquake_df
    earthquake_df = pd.DataFrame()
    for year in range(2010, 2024):

        for month in range(1, 13):

            start_date = f"{year}-{month:02d}-01"
            end_date = f"{year}-{month:02d}-30"
            query_parameters = {
                "format": "csv",
                "starttime": start_date,
                "endtime": end_date,
                "minmagnitude": "3",
                "limit": "20000"
            }
            # Hit the API and get the response
            response = requests.get(url, params=query_parameters)

            # If the response is successful, add the data to the earthquake_data DataFrame
            if response.status_code == 200:
                # Convert the CSV string to a pandas DataFrame
                csv_string = response.text
                df = pd.read_csv(StringIO(csv_string), header=None)

                # Assign column name

                # Append the data to the earthquake_data DataFrame
                earthquake_df = earthquake_df._append(df.iloc[1:, :])
                print(f"Appended for {start_date} to {end_date}")
                print("\n")

    earthquake_df.columns = [
        "time", "latitude", "longitude", "depth", "mag", "magType",
        "nst", "gap", "dmin", "rms", "net", "id", "updated", "place",
        "type", "horizontalError", "depthError", "magError", "magNst",
        "status", "locationSource", "magSource"
    ]

    directory = 'raw_data_From_api'
    if not os.path.exists(directory):
        os.makedirs(directory)


    file_path = os.path.join(directory,'alldata.xlsx')
    earthquake_df.to_excel(file_path, header=True, index=False)







def getting_data_as_df():
    return earthquake_df



