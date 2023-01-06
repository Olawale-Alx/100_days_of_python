import smtplib
import datetime as dt
import os

MY_EMAIL = os.environ.get('MY_EMAIL')
my_password = os.environ.get('SECRET')
# message = 'Hello, World'

with smtplib.SMTP_SSL(host='', port=0) as connection:
    # connection.starttls()
    connection.login(user=MY_EMAIL, password=my_password)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs='olaleyeolawale2020@outlook.com',
                        msg=f'Subject: Introduction\n\n\nHello, World. My email address is {MY_EMAIL}')

days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday',
        6: 'Sunday'}
now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week in days.keys():
    print(f'Yes, {days.get(day_of_week)}')
print(now.weekday())
