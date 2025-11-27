from datetime import datetime
dt=datetime.now() # 现在时间
print(dt)
dd=datetime(2007,5,6)
print(dd)
print(dd.year)
print(dd.month)
print(dd.day)
print(dd.hour)
print(dd.minute)
print(dd.second)
print(dt>dd) # 可以比较两个datetime时间先后
s=dt.strftime('%Y-%m-%d') # datetime -> string 这是datetime对象的函数
ss='2006-12-06'
dtim=datetime.strptime(ss,'%Y-%m-%d') # string -> datetime 这是datetime类型的函数
print(dtim)