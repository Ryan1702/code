a=list()
a.append(eval(input("请输入你的听力成绩:")))
a.append(eval(input("请输入你的口语成绩:")))
a.append(eval(input("请输入你的阅读成绩:")))
a.append(eval(input("请输入你的写作成绩:")))
b=["Listening","Speaking","Reading","Writing"]
ielts=dict(zip(b,a))
k=ielts.keys() # 这个叫做键，用来取每一项冒号左边的内容，就是听说读写
v=ielts.values() # 这个叫做值，用来取每一项冒号右边的内容，就是这四个数字
print("以下是键:")
for i in k: # 遍历键
    print(i)
print("以下是值:")
for i in v: # 遍历值
    print(i)
print("最大值为:",end='')
mx=max(v) # 取分数中的最大值
print(mx)