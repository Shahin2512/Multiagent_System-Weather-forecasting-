import requests

def get_next_launch():
    url = "https://api.spacexdata.com/v4/launches/next"
    res = requests.get(url)
    data = res.json()
    launchpad_id = data['launchpad']

    # Get launchpad details
    launchpad_res = requests.get(f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}")
    launchpad_data = launchpad_res.json()

    return {
        "name": data["name"],
        "date": data["date_utc"],
        "location": launchpad_data["locality"],
        "latitude": launchpad_data["latitude"],
        "longitude": launchpad_data["longitude"]
    }
