import requests


parameters = {
    'amount': 10,
    'type': 'boolean'
}

api_request = requests.get(url='https://opentdb.com/api.php', params=parameters)
data = api_request.json()
question_data = data['results']
