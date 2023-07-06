import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

api_url = os.getenv('OPENWEATHER_API_URL')
api_key = os.getenv('OPENWEATHER_API_KEY')


def get_forecast_data(place, forecast_days):
    url = f"{api_url}?q={place}&appid={api_key}"
    print(url)
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(response.json()['message'].title())

    data = response.json()
    forecast_list = data['list'][:forecast_days*8]

    forecast_dates = []
    forecast_temperatures = []
    forecast_weathers = []

    for day in forecast_list:
        forecast_dates.append(datetime.fromtimestamp(day['dt']).strftime("%Y-%m-%d %H:%M:%S"))
        # forecast_dates.append(day['dt_txt'])
        forecast_temperatures.append(float(day['main']['temp']) / 10)
        forecast_weathers.append(day['weather'][0]['main'])

    return {'dates': forecast_dates,
            'temperatures': forecast_temperatures,
            'sky': forecast_weathers
            }


def prepare_images_list(data):
    images = []
    for image in data:
        filename = f'images/{image.lower()}.png'
        images.append(filename)

    return images


if __name__ == "__main__":
    place = 'Londons'
    number_of_days = 3
    option = 'Temperature'
    data = get_forecast_data(place, number_of_days)
    print(data)
