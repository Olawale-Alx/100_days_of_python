# with open('text_file.txt') as file:
#     content = file.read()
#     print(content)

with open('new_file.txt', mode='w') as file:
    content = file.write('Test.')
    print(content)
