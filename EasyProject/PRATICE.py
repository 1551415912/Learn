S1 = "Let's go"
print(S1)
S2 = 'Let\'s go'
print(S2)
print("i love %s"%"chanyaoli")
s3="I was %d years old"
print(s3%22)
s4="My name is %s,I was %d years old"
print(s4%("changyaoli",22))
s5 = "i love {}".format("changyaoli")
print(s5)
for i in range(1,3):
    pass
    print("changyaoli")
benqian=10000
year=0
while benqian<15500:
    benqian=benqian*(1+0.067)
    year+=1
else:
    print("第{0}年拿了{1}元钱".format(year,benqian))