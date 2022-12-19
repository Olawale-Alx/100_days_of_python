import requests


api_request = requests.get(url='http://api.open-notify.org/iss-now.json')
status_code = api_request.status_code
data = api_request.json()
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

iss_current_position = (latitude, longitude)
print(iss_current_position)
