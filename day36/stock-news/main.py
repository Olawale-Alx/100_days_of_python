import requests
from twilio.rest import Client
import os


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
phone = os.environ.get('phone')

# # STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then
# print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python
# dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'apikey': os.environ.get('apikey')
}

api_request = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = api_request.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = float(data_list[0]['4. close'])
print(yesterday_data)

# Get the day before yesterday's closing stock price
day_before_data = float(data_list[3]['4. close'])
print(day_before_data)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive
# difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = round(yesterday_data - day_before_data, 2)

up_down = None
if difference > 0:
    up_down = '⬆️'
else:
    up_down = '⬇️'
# Work out the percentage difference in price between closing price yesterday and closing
#  price the day before yesterday.
percentage = round(difference / yesterday_data * 100, 2)
print(percentage)

if abs(percentage) > 5:

    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        'q': 'TSLA',
        'language': 'en',
        'sortBy': 'publishedAt',
        'apiKey': '39e05da2924d4020976a760aa9074a58'
    }
    news_request = requests.get(url='https://newsapi.org/v2/everything', params=news_params)
    # Use Python slice operator to create a list that contains the first 3 articles.
    news_data = news_request.json()['articles'][:3]
    # print(news_data)

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # Create a new list of the first 3 articles headline and description using list comprehension.
    messages_data = [f"""{STOCK_NAME}: {up_down}{round(percentage)}% Headline: {news['title']} Brief: {news['description']} {news['url']}"""
                     for news in news_data]

    # Send each article as a separate message via Twilio.
    for messages in messages_data:
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=messages,
                                         from_=phone,
                                         to='+2349039746629')

else:
    print('No news')
