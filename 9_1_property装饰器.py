class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # 访问器 getter方法
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    # 修改器 setter方法
    @age.setter
    def age(self, age):
        self._age = age
    
    def play(self):
        if self._age <= 16:
            print("%s正在玩飞行棋"%self._name)
        else:
            print("%s正在玩都地主"%self._name)
    
person = Person("王大锤",12)
person.play()
person.age = 25
person.play

print(person.name)