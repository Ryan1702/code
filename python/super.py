class a:
    kk=1234
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def show(self):
        print(self.age,self.name)
    @classmethod
    def show2(cls):
        print(cls.kk)
class b:
    k=2134
    def __init__(self,gender):
        self.gender=gender
    def sh(self):
        print(self.gender)
    @classmethod
    def shw(cls):
        print(cls.k)
class c(a,b):
    def __init__(self,age,name,gender,priv):
        a.__init__(self,age,name)
        b.__init__(self,gender)
        self.__priv=priv
        # 加一个下划线受保护，可以外部访问和修改
        # 加两个下划线是私有保护，只允许本类内部用，子类不能调用，外部更不能调用
    def ss(self):
        a.show(self)
        b.sh(self)
        # super().后面可以不用加self
        # 但是实际class名字后面需要加self
    def show(self): # 方法重写，在调用子类的show时会先看子类是否有定义，再看父类
        print(self.gender,end=' ')
        a.show(self)
    @property
    def password(self): # 用了@property就不用加括号了，私有属性变为可读但仍然不可以改
        return self.__priv
    def __str__(self): # 这也算方法重写，所有的类都有object这个父类，而该函数就是object有的
        return f'{self.gender} {self.name}'
def ok():
    print("OK!")
s=c(1,2,3,4)
s.ss()
print("-"*10)
print(s.kk,s.k)
print("-"*10)
print(s.password)
print("-"*10)
s.show()
print(s)
print("-"*10)
S=c(1,2,3,4)
S.pp=5 # 这个是动态绑定属性，直接创造新属性并赋值
print(S.pp)
print("-"*10)
S.ko=ok # 这个是动态绑定方法，用普通的ok函数迁移到S的ko方法中
S.ko()

# 多态
class cat():
    def p(self):
        print("cat")
class dog():
    def p(self):
        print("dog")
def printt(itm):
    itm.p()
ccc=cat()
ddd=dog()
printt(ccc)
printt(ddd)
# 不同类如果有同名方法，可以用同一方法调用
# 不在意我需要调用的对象是否是同一类