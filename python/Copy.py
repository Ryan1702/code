import copy
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,a,b):
        self.a = a
        self.b = b
a=A()
b=B()
c=C(a,b)
cc=c # 直接赋值全部一样
print(c,c.a,c.b)
print(cc,cc.a,cc.b)
ccc=copy.copy(c) # 浅拷贝，子类的地址不一样，父类地址一样
print(ccc,ccc.a,ccc.b)
cccc=copy.deepcopy(c) # 深拷贝，地址全都不一样
print(cccc,cccc.a,cccc.b)
# 地址一样意味着改了一个另外一个也会变