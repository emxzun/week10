# Полиморфизм принцип ООП

# Полиморфизм - возможность использовать один и тот же метод для объектов от разных классов, 
# при этом результат может меняться в зависимоти от того к какому классу принадлежит тот или иной объект.

# Полифморфизм - множество форм


# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print('Мяу')

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print('Гаф')


# cat1 = Cat('Барсик')
# dog1 = Dog('Рэкс', 20)
# # cat1.make_sound()
# # dog1.make_sound()
# list_obj = [cat1, dog1]
# for i in list_obj:
#     i.make_sound()



# class ShapeMixin: # Форма
#     def __init__(self, name) -> None:
#         self.name = name

#     def area(self): #Площадь
#         pass

#     def __str__(self):
#         return self.name


# class Square(ShapeMixin): # Квадрат
#     def __init__(self, name, h):
#         super().__init__(name)
#         self.h = h
#     def area(self):
#         return self.h ** 2


# class Circle(ShapeMixin): # Круг
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius**2


# s1 = Square('квадрат', 100)
# s2 = Square('квадрат2', 10)
# c1 = Circle('круг', 14)
# c2 = Circle('круг2', 2)
# print(s1)
# print(c2)
# list_ = [s1, s2, c1, c2]
# for i in list_:
#     print(i.area())
    
# def area_(x):
#     print(x.area())

# area_(s1)


# class A:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a

#     def __str__(self):
#         return self.name

# a1 = A('John', 23)
# print(a1)



# class MyStr(str):
#     def upper(self):
#         return 'John'

#     def __str__(self):
#         return super().__str__() + ' JahnPahn'


# str1 = MyStr('hello')
# print(str1.upper())
# print(str1)


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return f'Привет меня зовут {self.name} {self.last_name}'


class Employee(Person):
    def __init__(self, work, status):
        self.work = work
        self.status = status

    def get_info(self):
        return super().get_info(self) + f'. я работаю в копмании {self.company} копыта на должности {self.status}'



class Student(Person):
    def __init__(self, university, cours):
        self.university = university
        self.cours = cours

    def get_info(self):
        return super().get_info(self) + f'. я учусь в {self.university} на {self.cours} курсе'


employee = Employee('Pora', 'директора')
student = Student('КГТУ', 3)
person = Person('Иван', 'Петров')
print(student.get_info())
