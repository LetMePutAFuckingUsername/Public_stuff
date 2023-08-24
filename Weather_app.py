import requests
import pytz
import datetime
from datetime import datetime, timedelta

api_key = '9092b45c833173529140eba50bd420eb'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f'Temperature: \n'
          f'In Celsius: {temp_celsius:.2f} °C \n'
          f'In Fahrenheit: {temp_fahrenheit:.2f} °F \n')

#           -----------

    desc = data['weather'][0]

    main = desc['main']
    description = desc['description']
    id = desc['id']
    icon = desc['icon']

#           -----------

    print(f'Weather: \n'
          f'Main: {main} \n' 
          f'Description: {description} \n'
          f'ID: {id} \n'
          f'Icon: {icon} \n')

#           -----------

    coordinates = data['coord']
    lon = coordinates['lon']
    lat = coordinates['lat']

    print(f'Coordinates: \n'
          f'Longitude: {lon}\n'
          f'Latitude: {lat} \n')

#           -----------

    wind = data['wind']
    speed_mps = wind['speed']
    speed_kph = speed_mps * 3.6

    direction_degrees = wind['deg']
    compass_directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW",
                          "NNW"]

    direction_index = round(direction_degrees / 22.5) % 16
    compass_direction = compass_directions[direction_index]

    print(f'Wind:\n'
          f'Speed: {speed_kph:.2f} km/h\n'
          f'Direction: {compass_direction} ({direction_degrees:.2f}°) \n')

#           -----------

    clouds = data['clouds']
    cloudiness = clouds['all']

    print(f'Cloudiness: {cloudiness}% \n')

#           -----------

    timezone_offset = data['timezone']
    local_time = datetime.utcnow() + timedelta(seconds=timezone_offset)
    timezone = pytz.timezone('Etc/GMT{:+}'.format(timezone_offset // 3600))

    print(f'Local Time: {local_time.strftime("%Y-%m-%d %H:%M:%S")} ({timezone.zone}) \n')

#           -----------

    sys = data['sys']
    country = sys["country"]
    sunrise_timestamp = sys['sunrise']
    sunset_timestamp = sys['sunset']

    sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp)
    sunset_time = datetime.utcfromtimestamp(sunset_timestamp)

    print(f'Country: {country} \n'
          f'Sunrise: {sunrise_time} UTC \n'
          f'Sunset: {sunset_time} UTC \n')
else:
    print('Error fetching weather data')