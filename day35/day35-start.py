import requests
from twilio.rest import Client
import os
#
#
# parameters = {
#     'lat': '51.509865',
#     'lon': '-0.118092',
#     'units': 'metric',
#     'exclude': 'current,minutely,daily',
#     'appid': '6252037d47d60a4fd62b8900ba70f543'
# }
#
# api_request = requests.get(url='https://api.openweathermap.org/data/2.5/weather', params=parameters)
# data = api_request.json()
# print(data)
account_sid = os.environ.get('ACCOUNT_sid')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

parameters = {
    'lat': '30.6678211',
    'lon': '51.5797373',
    'appid': '85a5b35e1018fc162cf0fc2698d3bb0c'
}

api_requests = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
data = api_requests.json()['list'][:9]

will_rain = False

for three_hour_data in data:
    condition_data = three_hour_data['weather'][0]['id']
    if condition_data < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body='It is going to rain today. Come along with an umbrella ☂',
        from_='+12058394173',
        to='+2349039746629'
    )
    print(message.status)
# print(data)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sliced = numbers[1:10:2]
# print(sliced)
