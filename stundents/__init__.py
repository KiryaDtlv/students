# -*- encoding=utf-8 -*-
# This file was generated automatically
from .test import Semen, Katya, Diman, Svyat, MyPrint

__version__ = (1,0,0,0)

def prepare_objects():
    group_name: str = 'ИП-911'
    semen = Semen(group_name, 10)
    katya = Katya(group_name, 20)
    diman = Diman(group_name, 20)
    svyat = Svyat(group_name, 20)
    student_list = [semen, katya, diman, svyat]
    my_print = MyPrint(student_list)
    print(my_print)

def start():
    try:
        print("stundents v"+".".join(str(x) for x in __version__))
        prepare_objects()
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    start()
                