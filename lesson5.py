# class ToDo:
#     instances = {}

#     def __init__(self, task):
#         self.task = task

#     def give_priority(self, priority):
#         self.instances[priority] = self.task

#     def list_of_tasks(self):
#         return sorted(self.instances.items())


# obj1 = ToDo('сходить в кино')
# obj2 = ToDo('сделать дз')
# obj3 = ToDo('выгулять собаку')
# obj1.give_priority(4)
# obj2.give_priority(9)
# obj3.give_priority(1)
# print(obj1.instances)
# print(obj1.list_of_tasks())


### pagination 




# l = [{'id': 1},{'id': 2},{'id': 3},{'id': 4},{'id': 5}]

# def get_product(list_, page=1):
#     page -= 1
#     res = [[]]

#     page_index = 0
#     count_ = 0

#     for i in list_:
#         if count_ == 2:
#             res.append([])
#             page_index += 1
#             count_ = 0
#         count_ += 1

#         res[page_index].append(i)
#     return res[page]

# print(get_product(l))


class MyString(str):

    def __init__(self, s):
        self.s = s

    def append(self, new_string):
        self.s += new_string

    def pop(self):
        last_l = self.s[-1]
        self.s  = self.s[:-1]
        return last_l

    def __str__(self):
        return self.s


obj = MyString('String')
obj.append('hello')
print(obj.pop())
print(obj)