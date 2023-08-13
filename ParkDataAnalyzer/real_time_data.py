import requests


def get_data(facility_id):
    try:
        base_url = "https://p.hsl.fi/api/v1"
        if facility_id == "all":
            url_end = "/utilizations"
        else:
            url_end = f"/facilities/{facility_id}/utilization"
        api_url = base_url + url_end
        response = requests.get(api_url)
        if not response:
            return f"Facility with id: {facility_id} does not exist"
        return response.json()
    except:
        return f"There was a problem with getting data with id: {facility_id}"
