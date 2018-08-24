
'''
def printLine(row):
    for col in range(1, row + 1):
        print("{0}*{1}={2}".format(row, col, row * col), end="\t")
    print("\r")
#九九乘法表
for row in range(1, 10):
    printLine(row)
'''
'''
def stu(*args):
    print("大家好，我简单做下自我介绍")
    print(type(args))
    for item in args:
        print(item)
stu("常耀理",22,"安徽省阜阳市","邮政编码：236400")
'''
'''
def stu(**kwargs):
    print("大家好，我简单做下自我介绍")
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,"----",v)
stu(name="常耀理",age=22,addr="安徽省阜阳市")
print("*" * 20)
'''
"""
#收集参数混合调用案例
def stu(name,age,hobby="没有",*args,**kwargs):
    print("hello,大家好")
    print("我叫{0},我今年{1}岁了！".format(name,age))
    if hobby=="没有":
        print("我没有爱好，以后会有")
    else:
        print("我的爱好是{0}".format(hobby))
    print("*" *20)
    for i in args:
        print(i)
    print("#"*20)
    for k,v in kwargs.items():
        print(k,"----",v)
name="changyaoli"
age=22
stu(name,age,"footbal","安徽省",addr="阜阳市临泉县",work="student")
"""

###收集参数的解包问题
def stu(*args):
    n = 0  # 用来表示循环次数
    for i in args:
        print(type(i))
        print(n)
        n=n+1
        print(i)
l=list=["changyaoli",25,85,"liuxiujin"]
stu(*l)
'''
def stu1(name,age,*args):
    '
    这是文档
    hhhhhh
    jjjjjj
    llllll
    '
    print("这是函数文档")
print(help(stu1))
print(stu1.__doc__)
'''