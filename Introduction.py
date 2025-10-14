run=[31,29,31,30,31,30,31,31,30,31,30,31]
ping=[31,28,31,30,31,30,31,31,30,31,30,31]
def cc(s):
    ss=list(s)
    if(ss.count('.')!=2):
        return False
    pf=ss.index('.')
    if(pf==0):
        return False
    ss[pf]='/'
    ps=ss.index('.')
    if(ps==pf+1 or ps==len(s)-1):
        return False
    return True
def check_r(y):
    if(y%100==0):
        if(y%400==0):
            return True
        else:
            return False
    else:
        if(y%4==0):
            return True
        else:
            return False
def t(y,m):
    if(check_r(y)):
        print(y,run[m-1])
        return run[m-1]
    else:
        return ping[m-1]
def check(a):
    if(int(a[0])>2025):
        return False
    elif(int(a[1])<1 or int(a[1])>12):
        return False
    elif(int(a[2])<1 or int(a[2])>t(int(a[0]),int(a[1]))):
        return False
    return True
class birth:
    def __init__(self,y,m,d):
        self.y=y
        self.m=m
        self.d=d
    def age(self):
        return 2025-int(self.y)
class Person(birth):
    def __init__(self,name,y,m,d,gender,character):
        self.name=name
        super().__init__(y,m,d)
        self.gender=gender
        self.character=character
    def praise(self):
        print('Maybe we\'ve never met before. But I think',end=' ')
        if(self.gender=='Male'):
            print('you are so handsome.')
        elif(self.gender=='Female'):
            print('you are so pretty.')
        else:
            print('you are so smart.')
    def introduce(self):
        print('Hello everyone! My name is',self.name,end=' ')
        print('and my age is',self.age(),end='.\n')
        if(self.gender=='Male'):
            print('I\'m a boy who is',self.character,end='.\n')
        elif(self.gender=='Female'):
            print('I\'m a girl who is',self.character,end='.\n')
        else:
            print('I\'m so',self.character,end='.\n')
        print('My year of birth is',int(self.y),end='.\n')
        print('My month of birth is',int(self.m),end='.\n')
        print('My day of birth is',int(self.d),end='.\n')
name=input('What is your name? \n')
gender=input('What is your gender? Male or Female? \n')
while(gender!='Male' and gender!='Female'):
    print('The form is incorrect. Please rewrite it. ')
    print('If you don\'t want to show your gender', end=', ')
    print('please input \'Private\'. ')
    gender=input()
    if gender=='Private':
        break
s=input('Can you give me your birthday? Like \'2006.12.6\'. \n')
while(cc(s)==False):
    s=input('The form is incorrect. Please rewrite it. \n')
bir=s.split('.')
while(check(bir)==False):
    s=input('The form is incorrect. Please rewrite it. \n')
    while(cc(s)==False):
        s=input('The form is incorrect. Please rewrite it. \n')
    bir=s.split('.')
y,m,d=bir[0],bir[1],bir[2]
character=input('What is your character? Please use adjective phrases. \n')
person=Person(name,y,m,d,gender,character)
person.praise()
print('Please press \'Enter\' to continue.',end='')
while(input()!=''):
    print('Please only press \'Enter\' to continue.',end='')
print('###################################################')
print('# The self-introduction below have been produced. #')
print('###################################################')
person.introduce()
