# CRUD на миксинах
import json
from typing import List



class ReadDataMixin:
    def read(self, file_name: str) -> list:
        with open(file_name) as file:
            return json.load(file)

class CreateDataMixin:
    def create(self, file_name: str, data: List, **kwargs: dict) -> None:
        new_id = self.__find_max_id(data)
        data.append({'id': new_id, **kwargs})

        with open(file_name, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4) 

    def __find_max_id(self, data: List[dict]) -> int:
        if data:
            ids = [i['id'] for i in data] # [0, 1]
            return max(ids) + 1
        return 0


class UpdateDataMixin:
    def update_data(self, file_name, data: List[dict], id: int, **kwargs: dict) -> None:
        for i in data:
            if i['id'] == id:
                # to_delete = data.index(i)
                # data.pop(to_delete)
                i.update(**kwargs)
                break

        with open(file_name, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4) 
        

class DeleteDataMixin:
    def delete_data(self, file_name, data: List[dict], id: int) -> None:
        for i in data:
            if i['id'] == id:
                to_delete = data.index(i)
                data.pop(to_delete)
                break

        with open(file_name, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


class ToDo(ReadDataMixin, CreateDataMixin, UpdateDataMixin, DeleteDataMixin):
    def __init__(self, user_name: str) -> None:
        self.user_name = user_name
        self.file_name = user_name + '.json'
        try:
            self.__create_file()
        except FileExistsError:
            pass



    def __create_file(self) -> None:
        with open(self.file_name, "x") as file:
                json.dump([], file)



# john = ToDo('john')
# data_from_file = john.read(john.file_name)
# john.create(file_name=john.file_name, data=data_from_file, title='I need to do somthing')
# john.update_data(file_name=john.file_name, data=data_from_file, id=1, title='I need...', name='John')
# john.delete_data(file_name=john.file_name, data=data_from_file, id=0)

