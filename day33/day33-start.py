import requests


api_request = requests.get(url='http://api.open-notify.org/iss-now.json')
status_code = api_request.status_code
data = api_request.json()
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

iss_current_position = (latitude, longitude)
print(iss_current_position)

# parameters = {
#     'lat': 6.740147,
#     'lng': 3.422076,
#     'date': '2022-12-15',
#     'formatted': 0
# }
#
# api_request = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
# api_request.raise_for_status()
# data = api_request.json()
# sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
# sunset = data['results']['sunset'].split('T')[1].split(':')[0]
# print(f'Sunrise: {sunrise} Sunset: {sunset}')
