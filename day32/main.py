import smtplib
import datetime as dt
import random


MY_EMAIL = 'iolaleye62@yahoo.com'
recipient = 'iolaleye62@gmail.com'
subject = 'Today Motivation'
secret = 'vbovtfuubybpctnr'

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
