# Множественное наследование и миксины 

# class A:
#     name = 'John'

#     def __init__(self, age):
#         self.age = age
#         self.is_alive = True

#     def move(self):
#         return 'Go go go'


# class B(A):
#     name = 'Sam'

#     def move(self):
#         return super().move() + ' Hello'

# b = B(22)
# print(b.move())

# class Call:
#     def call(self):
#         print('Call...')

# class Mail:
#     def send_mail(self):
#         print('Отправляю сообщение')

# class SmartPhone(Call, Mail):
#     pass


# phone1 = SmartPhone()
# phone1.call()
# phone1.send_mail()
# print(isinstance(phone1, SmartPhone)) #True
# print(isinstance(phone1, Call)) #True
# print(issubclass(SmartPhone, Mail)) #True


# class Parent1:
#     a = 10


# class Parent2:
#     a = 15


# class Child(Parent1, Parent2):
#     a = 20

# john = Child()
# print(john.a)
# print(Child.mro())



# MRO - method resolution order(порядок разрешения методов)


# class A:
#     a = 1

# class B(A):
#     a = 2

# class C(A):
#     a = 3

# class D(C, B):
#     a = 4


# d = D()
# print(d.a)
# print(D.mro())
# print(D.__mro__)


# class GrandPa:
#     a = 1

# class GrandMa:
#     a = 2

# class Batya(GrandPa, GrandMa):
#     a = 3

# class Mom:
#     a = 4

# class Me(Batya, Mom):
#     a = 5

# obj = Me()
# print(obj.a)

###################################################

# Mixins

# Миксины - это особый вид множественного наследования.
# Задачей миксинов яляется расширение функционала других классов(расширители класса).

#1) Принято давать имена заканчивающиеся на Mixin: SendMainMixin
#2) От Mixin классов нельзя создавать объекты 
#3) Нужны чтобы расширить функционал другого класса(добавляя новую логику)


# class MoveMixin:
#     def move(self):
#         print('Двигаюсь')

# class StopMixin:
#     def stop(self):
#         print('Остановился')

# class Car(MoveMixin, StopMixin):
#     pass

# class Person(MoveMixin, StopMixin):
#     pass

# class PersonInitMixin:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

# class GetInfoMixin:
#     def get_info(self):
#         print(self.name, self.age)

# class GetYearMixin:
#     def get_year(self):
#         print(2022 - self.age)

# class Person(PersonInitMixin, GetInfoMixin, GetYearMixin):
#     pass


# sam = Person('Sam', 22)
# sam.get_info()
# sam.get_year()