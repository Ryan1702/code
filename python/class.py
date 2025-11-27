class Id:
    num=0 # 类属性，每个对象都能用
    def __init__(self,a,b):
        self.a=a # 实例属性，每个对象互不干扰
        self.b=b
        Id.num+=1
    def show(self): # 实例方法，必须带一个self
        print(self.a,self.b)
    # 调用的时候实例属性和实例方法都不需要写self
    @classmethod # 这个叫类方法，要用类名来定义，比如说Id
    def gn(cls):
        return cls.num
    @staticmethod # 静态方法，与对象无关，属于类的工具函数，不能调用实例
    def p():
        print("OK")
    # @语句只对后面一个def起作用
def introduction():
    print("Welcome")
x=Id(1,2)
y=Id(3,4)
x.show()
y.show()
x.gender="m"
print(x.gender)
Id.introduction=introduction # 类的动态绑定方法
Id.introduction()
print(Id.gn())
Id.p()