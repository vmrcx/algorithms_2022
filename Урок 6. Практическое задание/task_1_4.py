"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""

from pympler import asizeof

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return f"{self._length * self._width * 25 * 5 / 1000} T"

BC_OBJ = Road(20, 5000)
print(asizeof.asizeof((BC_OBJ)))  #328

class Road:
    __slots__ = ['_length', '_width']

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return f"{self._length * self._width * 25 * 5 / 1000} T"

BC_OBJ = Road(20, 5000)
print(asizeof.asizeof((BC_OBJ)))  #112