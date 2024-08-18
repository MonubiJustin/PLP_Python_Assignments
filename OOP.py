class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f'Hello, I am {self.name}, a {self.age} years old {self.gender}')


obj = Person('Justin Monubi', 19, 'male')
obj.introduce()