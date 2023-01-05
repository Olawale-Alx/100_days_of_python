import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 6.740147  # Your latitude
MY_LONG = 3.422076   # Your longitude
my_email = os.environ.get('MY_EMAIL')
recipient = 'olaleyeolawale2020@outlook.com'
secret = os.environ.get('SECRET')


def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and \
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def check_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    dark = time_now.hour

    if dark >= sunset or dark <= sunrise:
        return True


while True:
    # BONUS: run the code every 60 seconds
    time.sleep(60)
    # If the ISS is close to my current position, and it is currently dark
    if check_position() and check_time():
        # Then email me to tell me to look up.
        with smtplib.SMTP_SSL(host='smtp.mail.yahoo.com', port=465) as connection:
            connection.login(user=my_email, password=secret)
            connection.sendmail(from_addr=my_email, to_addrs=recipient,
                                msg='Subject: Look Up!!!\n\n\nOlawale,\n\nLook up!'
                                    'The ISS is in your location.')
