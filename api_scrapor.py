import requests
import json
# Define the API URL
api_url = "https://api.weatherapi.com/v1/history.json"

# Define the parameters
params = {
    "key": "3916bfa796744a6e9b4162633231912",
    "q": "Larache",
    "dt": "2023-01-01",
    "time_epoch": 1671517600
}

# Make API request
response = requests.get(api_url, params=params)
data = response.json()


for hour_data in data_from_api['forecast']['forecastday'][0]['hour']:
    hour_info = {
        'time': hour_data['time'],
        'temperature_c': hour_data['temp_c'],
        'wind_speed_kph': hour_data['wind_kph'],
        'wind_direction': hour_data['wind_dir'],
        'rain_precipitation_mm': hour_data['precip_mm'],
        'humidity': hour_data['humidity']
    }
    data['forecast']['forecastday'].append(hour_info)

# Convert the structured data to JSON
json_data = json.dumps(data, indent=2)

# Save the JSON data to a file
with open('weather_data.json', 'w') as json_file:
    json_file.write(json_data)

print("JSON data has been saved to 'weather_data.json'")