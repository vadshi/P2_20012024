"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...

# Значит должны быть значения по умолчанию у всех атрибутов
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезает бензина (capacity)
* "расход топлива на 100 км" (gas_per_100km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то бак заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```
выведет сообщение "проехали ... километров",
в результате поездки потратится бензин и увеличится пробег.
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать методы __str__ и __repr__
"""


class Car:
    def __init__(self, gas=0, capacity=50, gas_per_100km=12, mileage=0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = mileage

    def fill(self, liter: float | int) -> None:
        if self.gas + liter <= self.capacity:
            self.gas += liter
            print(f'В баке {self.gas} литров')
        else:
            print(f'Бак полный, лишний бензин: {self.gas - self.capacity + liter} литров')
            self.gas = self.capacity

    def ride(self, kilometers: float | int) -> None:
        curr_range = self.gas / self.gas_per_100km * 100
        if curr_range >= kilometers:
            print(f'Проехали {kilometers} километров')
            self.gas = self.gas - (kilometers / 100 * self.gas_per_100km)
            self.mileage += kilometers
        else:
            self.mileage += curr_range
            print(f'Проехали {round(curr_range, 2)} километров')
            self.gas = 0

    def __repr__(self) -> str:
        return f'Car({self.gas},{self.capacity},{self.gas_per_100km},{self.mileage})'

    def __str__(self) -> str:
        return (f'Машина с параметрами:\n'
                f'  - бензин = {self.gas}л\n'
                f'  - пробег = {self.mileage}км')


# Тестовая часть
car = Car(5, 50, 10, 1000)
print(repr(car))

car.fill(20)
print(car)
print('=' * 30)

car.ride(150)
print(car)
print('=' * 30)

car.fill(100)
print(car)
print('=' * 30)

car.ride(1500)
print(car)
print('=' * 30)
