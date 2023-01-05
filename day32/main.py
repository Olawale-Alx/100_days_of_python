import smtplib
import datetime as dt
import random
import os


MY_EMAIL = os.environ.get('MY_EMAIL')
recipient = 'iolaleye62@gmail.com'
subject = 'Today Motivation'
secret = os.environ.get('SECRET')

now = dt.datetime.now()
day = now.weekday()
if day == 0:
    with open('quotes.txt') as quotes:
        quote = quotes.readlines()
        message = random.choice(quote)

        with smtplib.SMTP_SSL(host='smtp.mail.yahoo.com', port=465) as connection:
            connection.login(user=MY_EMAIL, password=secret)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=recipient,
                                msg=f'Subject:{subject}\n\n\n{message}')
