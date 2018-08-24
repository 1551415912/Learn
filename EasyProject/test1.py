'''
a1=100
def fun():
    print(a1)
    print("*" *10)
    a=22
    print(a)
print(a1)
fun()
'''
'''
def fun():
    global b1
    b1=100
    print(b1)
    print("*" *10)
    a=22
    print(a)
fun()
print(b1)
'''
'''
#eval()函数,把字符串当成表达式来执行，返回表达式执行后的结果；
#exec()函数,把字符串当成表达式来执行，不返回表达式执行后的结果；
x=100
y=200
z1=x+y
z2=eval("x+y")
print(z1)
print(z2)
'''
'''
#递归函数(Python对递归函数深度有限制，超过限制则报错)
x=0
def fun():
    global  x
    x=x+1
    print(x)
    fun()
fun()
'''
'''
#斐波那契数列
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))
'''
'''
#list:一组有顺序的数据的组合
l1=[100,200,300,400,500,600]
print(type(l1))
print(l1[2:5])#注意范围：包含左边，不包含右边
print(l1[5:])
print(l1[1:5:2])#最后面的数字可以代表增长速度(增长幅度可以为负值，则顺序从右往左)
print(l1[1:20])#下标可以超出范围，超出后不再考虑多余下标内容
print(l1[1:-1])#规定数组最后一个数字的下标是-1
print(l1[-2:-4])#要从左往右
print(l1[-2:-4:-1])
#分片操作是生成一个新的list
del l1[1]
print(l1)
'''
"""
#汉诺塔问题
def hano(n,a,b,c):
    '''
    汉诺塔的递归实现
    :param n: 代表几个盘子
    :param a: 代表第一个塔
    :param b: 代表第二个塔
    :param c: 代表第三个塔
    '''
    if n==1:
        print(a,"----",c)
        return None
    '''
    if n==2:
        print(a,"----",b)
        print(a,"----",c)
        print(b,"----",c)
        return None
    '''
    hano(n-1,a,c,b)
    print(a,"----",c)
    hano(n-1,b,a,c)
a="A"
b="B"
c="C"
n=2
hano(n,a,b,c)
"""
"""
a=[1,2,3,1,4,6]
b=[7,8,9,10]
c=a+b
print(c)
a=[["one",1],["two",2],["three",3]]
for k,v in a:
    print(k,"----",v)
a=[1,2,3,4,5]
b=[i*10 for i in a]
print(b)
a=[x for x in range(100,400) if x%100==0]
print(a)
b=[x for x in range(1,4)]
print(b)
c=[m+n for m in a for n in b ]#相当于两个for嵌套
print(c)
for m in a:
    for n in b:
        print(m+n,end="  ")
print()
a=[11,2,3,4,15,6,7,8,9]
print(len(a))
print(max(a))
print(min(a))
"""
"""
a=[i for i in range(1,5)]
print(a)
a.append(100)#插入一个内容，在末尾添加
print(a)
a.insert(3,666)#insert(index,data)
print(a)
print(a.pop())#pop,从对位拿出一个元素，即把最后一个元素取出来
print(a)
a.remove(1)
print(a)
a.reverse()
print(a)
#count():查找列表中的指定值或者元素的个数
#copy():
a=[1,2,3,4,5,6]
b=a
b[1]=100
print(a)
print(b)
b[4]=10
b=a.copy()
print(a)
print(b)
"""
"""
#copy函数是个浅拷贝函数，即只拷贝一层内容
a=[1,2,3,[4,5,6]]
b=a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
"""
"""
#元组tuple:元组可以看成一个不可更改的list
t=(1,2,3,4,5)
print(type(t))
print(t)
t=1,2,3,4,5
print(type(t))
print(t)
l=[1,2,3,4,5]
t=tuple(l)
print(type(t))
print(t)
#元组的特性：是序列表，可以访问，不可修改，数据可以是任意类型；
t=(1,2,3,4,5)
print(t[3])
t1=t[1::2]
print(t1)
t2=t[2:100]#切片可以超标
print(t2)
#序列相加
t1=(1,2,4)
t2=(3,5,6)
t1=t1+t2#传址操纵
print(t1)
#元组相乘
t1=1,2,3
t=t1*3
print(t)
for i in t:
    print(i,end="\t")
print()
t=((1,2,3),(4,5,6),(7,8,9))
for i in t:
    print(i,end="\t")
print()
for k,m,n in t:
    print(k,"---",m,"---",n)
"""
"""
t=(1,2,3,4,5,6)
print(len(t))
print(max(t))
print(min(t))
print(any(t))
a=1
b=3
print(a)
print(b)
print("*" *20)
a,b=b,a
print(a)
print(b)
"""
"""
s={1,2,3,4,5}#如果没有值，则定义的是dict类型
print(type(s))
print(s)
s={1,2,3,4,5,6,7,8,9}
print(s)
s.pop()
print(s)
"""
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
s_1 = s1.intersection(s2)  # 交集
print(s_1)
s_2 = s1.difference(s2)  # 差集
print(s_2)
s_3 = s1.issubset(s2)  # 检查一个子集是否为另一个子集
print(s_3)
d1 = dict(one=1, two=2, three=3)
print(d1)
d2 = {"one": 1, "two": 2, "three": 3}
print(d2["one"])
d2["one"] = 6
print(d2)
del d2["one"]
print(d2)
