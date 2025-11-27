import time
now=time.time() # 时间戳
time.sleep(1)
print(now)
time.sleep(1)
n=time.localtime() # 本地时间
print(n)
time.sleep(1)
nn=time.localtime(180) # 从1970.1.1 7:30开始多少秒
print(nn)
time.sleep(1)
nnn=time.ctime(0)
print(nnn)
time.sleep(1)
print(time.strftime('%Y-%m-%d %H/%I:%M:%S %B %A',nn))
time.sleep(1)
# 以上函数是将类型从struct_time -> string
print(time.strptime('2007-05-06','%Y-%m-%d'))
time.sleep(1)
# 以上函数是取string中的值，利用相同的格式，转化为struct_time