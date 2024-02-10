
class Student:
    """ Test class for learning """
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property    
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None
    
    @property    
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None
    
    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = f'{self._name} {self._surname}'
        return self._full_name

    # Можно, но не нужно. property <name> не работает
    # def name(self):
    #     print('Hello')


s = Student('Ivan', 'Ivanov')
print(s.name)
print("before", s.__dict__)
print(f'{s.full_name = }')
print("after", s.__dict__)

print('*' * 40)

s.surname = 'Petrov'
print(s.__dict__)
print(f'{s.full_name = }')
print(s.__dict__)

print('*' * 40)
s.name = 'Petr'
print(s.__dict__)
print(f'{s.full_name = }')
print(s.__dict__)
