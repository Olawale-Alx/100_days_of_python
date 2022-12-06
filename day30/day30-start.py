# try:
#     with open('a_file.txt', mode='r') as a_file:
#         a_file.read()
#
# except FileNotFoundError as error_message:
#     print(f'{error_message}: This file does not exist!')
#
# try:
#     text = 100
#     print(text + 5)
# except TypeError:
#     print(f'text variable cannot be added to a integer')
# else:
#     print(text + 2)
# finally:
#     print(5 * 3)

fruits = ['Apple', 'Pear', 'Orange']


# # TODO: Catch the exception and make sure the code runs without breaking
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print('fruit pie')
#     else:
#         print(f'{fruit} pie')
#
#
# make_pie(6)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Likes': 19, 'Comments': 3}
]

posts_likes = 0
for post in facebook_posts:
    try:
        posts_likes += post['Likes']
    except KeyError:
        post['Likes'] = 0

print(posts_likes)
