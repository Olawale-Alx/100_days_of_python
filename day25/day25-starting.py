import pandas

# import csv
#
#
# with open('./weather_data.csv', mode='r') as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for each_row in data:
#         if each_row[1] != 'temp':
#             temperatures.append(int(each_row[1]))
#
#     print(temperatures)

# data = pandas.read_csv('weather_data.csv')
# temp_data = data['temp']
# temp_data = data['condition']
# for temp in temp_data:
#     print(f'The weather forecast today is a {temp} condition')
# TODO 1: Calculate the average of the temperature data
#
#
# def summation(num_total):
#     sum_total = 0
#     for q in num_total:
#         sum_total = sum_total + q
#     return sum_total
#
#
# temp_summation = summation(temp_data)
# print(temp_summation)
# temp_average_data = round(temp_summation/len(temp_data), 2)
# print(temp_average_data)
# temp_average_data = temp_data.mean()
# print(temp_average_data)
#
# # TODO 2: Get the max of the temp_data series
# temp_max_data = temp_data.max()
# print(temp_max_data)
#
# # TODO 3: Get the max of the temp_data series
# temp_min_data = temp_data.min()
# print(temp_min_data)
#
# # TODO 4: Get the row of data when the weather temp is at maximum
# print(data[data.temp == temp_max_data])
#
# # TODO 4: Get the row of data when the weather temp is at minimum
# print(data[data.temp == temp_min_data])
#
# # TODO 5: Get the temperature condition for monday and convert the data to Fahrenheit
# monday = data[data.day == 'Monday']
# celsius_monday = int(monday['temp'])
#
# # convert to fahrenheit
# fahrenheit_monday = (celsius_monday * 9 / 5) + 32
# print(fahrenheit_monday)

# TODO 6: Read a squirrel data file, get the total of all colors in the csv file and save the output to a csv file
data = pandas.read_csv('central_park_squirrel_data.csv')
fur_color = data['Primary Fur Color']
# print(fur_color)
grey = 0
black = 0
cinnamon = 0
no_color = 0
for color in fur_color:
    # print(color)
    if color == 'Gray':
        grey += 1
    elif color == 'Black':
        black += 1
    elif color == 'Cinnamon':
        cinnamon += 1
    else:
        no_color += 1
# print(grey, black, cinnamon, no_color)
fur_color_data = {'Fur Color': ['Gray', 'Black', 'Cinnamon', 'No Color'],
                  'Count': [grey, black, cinnamon, no_color]
                  }
color_data = pandas.DataFrame(fur_color_data)
color_data.to_csv('squirrel_color_count.csv')
