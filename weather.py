from dataclasses import dataclass
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv('API_KEY')

@dataclass
class WeatherData:
    main:str
    description:str
    icon:str
    temperature:float

'''
    Get latitude and longitude of a specific place
    Arguments:
        city_name: a string 
        state_code: a string
        country_code: a string
        API_key: a string 
    Retuns:
        lat: a float 
        lon: a float
    '''

def get_lat_log(city_name, state_code, country_code, API_key):
    resp=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}").json()
    data=resp[0]    
    lat, lon=data.get('lat'), data.get('lon')
    return lat, lon
    
def get_current_weather(lat,lon, API_key):
    resp=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric").json()
    #print(resp.get('main'))
    return WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=resp.get('main').get('temp')
    )

def main(city_name, state_name, country_name):
    lan,lon=get_lat_log(city_name, state_name, country_name, api_key)
    return get_current_weather(lan,lon, api_key)
