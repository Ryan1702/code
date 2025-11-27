a,b=10,20
sum=a.__add__(b)
sub=a.__sub__(b)
mul=a.__mul__(b)
div=a.__truediv__(b)
print(sum,sub,mul,div)
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,x,y):
        self.x=x
        self.y=y
class D:
    pass
class E:
    pass
class F(D,E):
    pass
class G(C,F):
    pass
c=A()
d=B()
e=C(1,2)
print(type(c),type(d),type(e))
print(c.__dict__)
print(d.__dict__)
print(e.__dict__)
print(c.__class__,d.__class__,e.__class__)
print(A.__bases__,B.__bases__,C.__bases__)
print(A.__base__,B.__base__,C.__base__)
print(A.__mro__,B.__mro__,C.__mro__)
print(G.__mro__)
print(A.__subclasses__(),B.__subclasses__(),C.__subclasses__())
print(G.__subclasses__())