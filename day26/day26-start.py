# name = 'Olawale'
# new_list = [n for n in name]
# print(new_list)

# items = []
# for a in range(1, 5):
#     a *= 2
#     items.append(a)
# print(items)

# item_in_range = [i * 2 for i in range(1, 5)]
# print(item_in_range)

# name = input('Enter your name:\n')
# name_list = [letter for letter in name if (name != 'ola')]
# print(name_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
name_list = [name.upper() for name in names if (len(name) > 5)]
print(name_list)
