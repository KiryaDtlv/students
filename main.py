from abc import ABC, abstractmethod
from typing import List

class Student(ABC):
    def __init__(self, group_name: str, age: int):
        self.name: str = self.__class__.__name__
        self.age: int = age
        self.group_name: str = group_name

    def __repr__(self) -> str:
        return f'Я {self.name} из {self.group_name} мне {self.age}'

    @abstractmethod
    def study(self) -> str:
        ...


class Katya(Student):
    def study(self) -> str:
        return f'Хожу на все пары'


class Semen(Student):
    def study(self) -> str:
        return f'Мне похуй, сижу в шкафу вместо пар'


class Diman(Student):
    def study(self) -> str:
        return f'В футбол играю ёпта'


class Svyat(Student):
    def study(self) -> str:
        return f'Я {self.name} и ворчу на парах'


class MyPrint:
    def __init__(self, stundent_list: List[Student] = []):
        self.student_list = stundent_list
    
    def __repr__(self) -> str:
        text = ''
        for student in self.student_list:
            text += f'''
###########
{student}
{student.study()}
###########\n
            '''
        return text
            

    def push_student(self, student: Student):
        self.student_list.append(student)



if __name__ == '__main__':
    group_name: str = 'ИП-911'
    semen = Semen(group_name, 10)
    katya = Katya(group_name, 20)
    diman = Diman(group_name, 20)
    svyat = Svyat(group_name, 20)
    student_list = [semen, katya, diman, svyat]
    my_print = MyPrint(student_list)
    print(my_print)