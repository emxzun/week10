# Магические методы
    # Дандер методы
    # Супер методвы
    # Служебные методы

# Магические методы - это в первую очередь те методы у которых __ в начале и __ в конце, 
# срабатывают эти методы автоматически при выполнении какой-то операции (+, -, <>, *, / и т.д), 
# мы можем добавлять какой-то новый функционал - свою логику

# Магические методы необходимы для того, 
# чтобы определяемые наши объекты могли работать с некоторыми оператарами или же встроенными функциями 



# class User:
#     def __new__(cls, *args, **kwargs):
#         print('New worked')
#         return super().__new__(cls)

#     def __init__(self, email):
#         print('Init worked')
#         self.email = email

#     def __str__(self):
#         return self.email

#     def __del__(self):
#         print('Del worked')

# user1 = User('e23434@mail.com')
# print(user1)



# class Word(str):
#     def __new__(cls, *args, **kwargs):
#         s = args[0]
#         s = s.replace(' ', '')
#         return super().__new__(cls, s)

# word1 = Word('a b c')
# print(word1)




# class User:
#     def __init__(self, email):
#         self.email = email

#     def __str__(self):
#         return self.email

#     def __repr__(self):
#         return self.email

# user1 = User('ewfe@gmail.com')
# print(user1)
# print(repr(user1))
# print(user1.__repr__())


# eval




# a = 'sad'
# print(a)
# print(repr(a))
# a = 'input()'
# print(a)
# print(eval(a))


# import datetime
# print(repr(datetime.date.today()))




# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return f'Это + и результат равен: {self.value + other}'

#     def __sub__(self, other):
#         return f'Это - и результат равен: {self.value - other}'

#     def __mul__(self, other):
#         return  f'Это * и результат равен: {self.value * other}'

#     def __truediv__(self, other):
#         return  f'Это / и результат равен: {self.value / other}'

#     def __floordiv__(self, other):
#         return  f'Это // и результат равен: {self.value // other}'


#     def __mod__(self, other):
#         return  f'Это % и результат равен: {self.value % other}'


#     def __pow__(self, other):
#         return  f'Это ** и результат равен: {self.value ** other}'

#     def __radd__(self, other): # говорит что объект справа r - right
#         return  f'Это ** и результат равен: {self.value ** other}'

# num = MyNumber(5)
# print(num + 1) # 
# print(num - 1)
# print(num * 5)
# print(num / 2)
# print(num // 2)
# print(num % 3)
# print(num ** 5)
# print(4 ** num)





# class Employee:
#     def __init__(self, name, salary, rating):
#         self.name = name
#         self.salary = salary
#         self.rating = rating

#     def __gt__(self, other): # Great Them сравнивает что больше
#         return self.rating > other.rating

#     def __lt__(self, other):
#         return self.rating < other.rating


#     def __eg__(self, other): # ==
#         return self.rating == other.rating

#     def __ge__(self, other): # >=
#         return self.rating >= other.rating

#     def __le__(self, other): # <=
#         return self.rating <= other.rating

#     def __ne__(self, other): # не равно !=
#         return self.rating != other.rating

# john = Employee('John', 25, 9)
# sam = Employee('Sam', 40, 10)
# print(john > sam)
# print(john < sam)
# print(john == sam)
# print(john >= sam)
# print(john <= sam)
# print(john != sam)





# class NewClass:
#     def __init__(self, name):
#         self.name = name

#     def __int__(self):
#         print('hello')
#         return 100

#     def __bool__(self):
#         print('Hello')
#         return True


# a = NewClass('5')
# print(int(a))
# print(bool(a))

############################################################################################

# class A:
#     def __setattr__(self, name, value):
#         value = value.upper()
#         return super().__setattr__(name, value)

#     def __delattr__(self, name):
#         print('Deleted')
#         return super().__delattr__(name)

# obj1 = A()
# obj1.f = 'John'
# del obj1.f
# print(obj1.f)



# class A:
#     def __init__(self):
#         self.l = [1,2,3]


#     def __getitem__(self, index):
#         return self.l[index]

#     def __setitem__(self, index, value):
#         self.l[index] = value

#     def __delitem__(self, index):
#         return 'Я удаляю'

# a = A()
# print(a[0])
# a[0] = 'Hello'


# class A:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#         self.__l = []

# obj1 = A(name='John', age=22)
# print(obj1.__dict__)



# __getattr__ - вызывается тогда когда мы пытаемся вызвать атрибут который еще не был определен 
# __getattribute__ - 



# import datetime
# dt = datetime.datetime.now()
# strf_ = dt.strftime('%H:%M:%S:%f')
# print(strf_)