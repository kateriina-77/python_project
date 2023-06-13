import pandas as pd
import requests
import json

file_path = "data/parsing_data.json"
url = "https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.62&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,weathercode,surface_pressure,visibility,windspeed_10m&past_days=14&forecast_days=1"

def get_data(url, file_path):
    response = requests.get(url)
    data = response.json()

    with open(file_path, "w") as json_file:
        json.dump(data, json_file)
        
    return data


def create_dataframe_from_json(file_path, data):
    with open(file_path, "r") as file:
        json_data = json.load(file)

    return pd.DataFrame(data["hourly"])
