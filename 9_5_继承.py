class Person(object):
    __slots__ = ("_name", "_age")
    def __init__(self, name, age):
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
    
    def play(self):
        print("%s正在玩耍"%self._name)

    def watch_av(self):
        if self._age >= 18:
            print("可以看")
        else:
            print("不能看")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    
    @property
    def grade(self):
        return self._grade 
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade 

    def study(self, course):
        print("%s的%s正在学习%s"%(self._grade, self._name, course))

class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))

def main():
    stu = Student("王大锤", 15, "初三")
    stu.study("数学")
    stu.watch_av()

    tea = Teacher("罗浩", 38, "专家")
    tea.teach("计算机")
    tea.watch_av()

if __name__ == "__main__":
    main()