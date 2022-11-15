# with open('text_file.txt') as file:
#     content = file.read()
#     print(content)

# with open('text_file.txt', mode='a') as file:
#     content = file.write('\nThis is 100 days of Python.')
#     print(content)

# with open('some_text.txt', mode='w+') as file:
#     file.write('This is Ola\n')

with open('text_file.txt', mode='r') as filed:
    # filed.write('\nAfrica')
    print(filed.read())

try:
    with open('/home/vagrant/Documents/testmd5.txt', mode='r') as file:
        content = file.read()
    print(content)

except FileNotFoundError:
    print('File not found.')
