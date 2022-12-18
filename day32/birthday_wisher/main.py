import smtplib
import datetime as dt
import random
import pandas

my_email = 'iolaleye62@yahoo.com'
recipient = 'olaleyeolawale2020@outlook.com'
secret = 'vbovtfuubybpctnr'
subject = 'Happy Birthday'

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
now = dt.datetime.now()
today = (now.month, now.day)

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv('birthdays.csv')

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formatted like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
birthdays_dict = {(data['month'], data['day']): data for (index, data) in data.iterrows()}

# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if today in birthdays_dict:
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    birthday_person = birthdays_dict[today]
    with open(file_path, mode='r') as letters:
        letter = letters.read()
        letter.replace('[NAME]', birthday_person['name'])

    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: The message should have the Subject: Happy Birthday then after \n\n The Message Body.
    with smtplib.SMTP_SSL(host='smtp.mail.yahoo.com', port=465) as connection:
        connection.login(user=my_email, password=secret)
        connection.sendmail(from_addr=my_email, to_addrs=recipient,
                            msg=f'Subject: {subject}\n\n\n{letter}')

else:
    print(False)

