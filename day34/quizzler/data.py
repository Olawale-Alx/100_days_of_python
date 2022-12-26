import requests


parameters = {
    'amount': 50,
    'type': 'boolean',
    'category': 18
}

api_request = requests.get(url='https://opentdb.com/api.php', params=parameters)
data = api_request.json()
question_data = data['results']
