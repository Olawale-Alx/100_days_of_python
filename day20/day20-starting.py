class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Breathe in, Breathe out')


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print('and calm down')

    def legs(self, name):
        print(f'{name} has four legs')


dog = Dog()
eye = dog.num_eyes
print(eye)
dog.breathe()
dog.legs('Brian')
