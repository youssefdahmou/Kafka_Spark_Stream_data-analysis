import requests
import json
import time
from confluent_kafka import Producer


kafka_config = {
    'bootstrap.servers': 'localhost:9092',  
    'client.id': 'weather-producer'
}

api_url = "https://api.weatherapi.com/v1/history.json"
params = {
    "key": "3916bfa796744a6e9b4162633231912",
    "q": "Larache",
    "dt": "2023-01-01",
    "time_epoch": 1671517600
}
kafka_topic = 'weather_kafka_topic'

# Function to fetch data from the API, filter, and publish to Kafka
def fetch_filter_and_publish():
    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        filtered_data = {
    'datetime': data['location']['localtime'],
    
        'name': data['location']['name'],
        'country': data['location']['country'],
        'latitude': data['location']['lat'],
        'longitude': data['location']['lon'],
        'timezone': data['location']['tz_id'],
        'max_temp_c': data['forecast']['forecastday'][0]['day']['maxtemp_c'],
        'min_temp_c': data['forecast']['forecastday'][0]['day']['mintemp_c'],
        'avg_temp_c': data['forecast']['forecastday'][0]['day']['avgtemp_c'],
        'max_wind_mph': data['forecast']['forecastday'][0]['day']['maxwind_mph'],
        'avg_visibility_km': data['forecast']['forecastday'][0]['day']['avgvis_km'],
        'avg_humidity': data['forecast']['forecastday'][0]['day']['avghumidity'],
        'uv_index': data['forecast']['forecastday'][0]['day']['uv']
    }
        producer.produce(kafka_topic, json.dumps(filtered_data))

        print("Filtered data published to Kafka topic:", kafka_topic)

    except Exception as e:
        print(f"Error: {e}")

producer = Producer(kafka_config)

while True:
    fetch_filter_and_publish()
    time.sleep(9)  # 900 seconds = 15 minutes