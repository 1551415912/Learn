"""
class Student(object):
    '''
    #属性案例
    #创建Student类，描述学生类
    #学生具有Student.name属性，但是name格式不统一
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.setName(name)


    #介绍下自己
    def intro(self):
        print("Ha,my name is {0}, And my age is {1}".format(self.name, int(self.age)))

    def setName(self, name):
        self.name = name.upper()


s1 = Student("Liu Ming", 19.8)
s2 = Student("Chang Ming", 24)
s1.intro()
s2.intro()
print(Student.__doc__)
print(Student.__dict__)
print(Student.__name__)
print(Student.__bases__)
"""

"""
class A(object):
    def __init__(self):
        print("大家好")

    def __call__(self):
        print("ABA")

    def __str__(self):
        return "Chang yao li"

    def __getattr__(self, item):
        print("没找到这个值")
        print(item)

a = A()
a()
print(a)
print(a.name)
"""

"""
class Person():
    #实例方法
    def eat(self):
        print(self)
        print("Eating......")

    #类方法
    @classmethod
    def Play(cls):
        print(cls)
        print("Playing......")

    #静态方法
    @staticmethod
    def say():
        print("Saying......")


yue = Person()

#实例方法
yue.eat()
#类方法
Person.Play()
yue.Play()
#静态方法
Person.say()
yue.say()
"""


