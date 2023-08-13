import json
from time import sleep

import requests

import DataSaver

def poll_data(polling_interval, facility_ids):
    base_url = "https://p.hsl.fi/api/v1/facilities"
    previous_timestamp = None
    while True:
        # Go through all the ids given in config
        for f_id in facility_ids:
            try:
                url_end = f"/{f_id}/utilization"
                api_url = base_url + url_end
                response = requests.get(api_url)
                # Log the response
                print(response.json())

                # If timestamp have changed find the desired information from the response
                response_dict = json.loads(response.text)[0]
                latest_timestamp = response_dict["timestamp"]
                if latest_timestamp != previous_timestamp:
                    previous_timestamp = latest_timestamp
                    DataSaver.write_to_file(response_dict["facilityId"], response_dict["capacity"],
                                            response_dict["spacesAvailable"], latest_timestamp)
            except:
                print(f"There was a problem with api response for id {f_id}")

        sleep(polling_interval)
