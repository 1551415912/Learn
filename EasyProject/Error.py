'''
while True:
    try:
        
        print(x)
        break
    except ValueError:
        print("非数值，请重新输入")
'''
"""
while True:
    try:
        x = int(input("请输入被除数："))
        y = int(input("请输入除数："))
        print(x/y)
    except ValueError:
        print("输入的必须是数字")
        break
    except ZeroDivisionError:
        print("除数不能为0")
        break
"""
"""
while True:
    try:
        x = int(input("请输入被除数："))
        y = int(input("请输入除数："))
    except ValueError:
        print("必须输入数字")
        break
    else:
        try:
            z=x/y
        except ZeroDivisionError:
            print("除数不能为0")
        else:
            print(z)
"""
"""
while True:
    try:
        f = open("a.txt")
        line1 = f.readline()
        x = int(line1)
    except ValueError:
        print("第一行的值不是数字")
        break
    else:
        print(x)
        break
    finally:
        print("最后执行了清理，关闭了文本文件。 ")
        f.close()
"""
with open("a.txt") as f:
    line1 = f.readline()
    x = int(line1)
    print(x)