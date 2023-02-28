import requests

API_KEY = "72ebf31a3d91a50388e12c0ddcd1bd9f"


def get_data(place, forcast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo", forcast_days=3))
