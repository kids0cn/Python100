from abc import ABCMeta, abstractmethod


# 抽象类，就是不能创建对象的类，专门为了让其他的类去继承它
class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod # 抽象方法，实例化要重写
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print("%s:旺旺"%self._nickname)


class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pet = Dog("大黄")
    pet.make_voice()
    pet = Cat("凯迪")
    pet.make_voice()

    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()
