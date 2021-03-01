class Person(object):
    # 限定Person类能够绑定的对象
    __slots__ = ("_name", "_age", "_gender")

    def __init__(self, name ,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self)

