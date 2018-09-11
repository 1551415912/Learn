class Animel():
    def __init__(self) -> object:
        print("Animel")


class PaxingAni(Animel):
    def __init__(self) -> object:
        print("Pai xing dongwu")


class Dog():
    def __init__(self) -> object:
        print("I am init in dog")


class Cat(PaxingAni):# Cat()没有写构造函数，需要向上查找父类的构造函数
    pass
