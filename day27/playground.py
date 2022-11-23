# *args
def add(*args):
    sum_total = 0
    for num in args:
        sum_total = sum_total + num
    print(sum_total)


add(1, 2, 3, 6, 10, 89)


# **kwargs
def animal_data(specie, **kwargs):
    print(f'Specie: {specie}, Personal_Date: {kwargs}')


animal_data(specie='Caucasian', name='Dog', skin='yellow', health_bar=100)
animal_data(specie='Shepherd')
