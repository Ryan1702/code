def cop(file,path,t):
    a=open(file,'r',encoding='utf-8') # 如果是图片的话改成rb，encoding去掉
    b=open(path,'w',encoding='utf-8') # 如果是图片的话改成wb，encoding去掉
    b.write(a.read())
    b.close() # 可以用with来省去这个close
    a.close() # 例如以下的例子就不需要close
    with open(t,'w+') as f:
        l=[
            ['1','2'],
            ['3','4'],
            ['5','6']
        ]
        for line in l:
            f.write(','.join(line))
            f.write('\n')
def pic(file,path):
    a=open(file,'rb')
    b=open(path,'wb')
    s=a.read()
    b.write(s)
    b.close()
    a.close()
cop('try.txt','try_copy.txt','with.csv')
# csv文件是表格，输入只能输入字符串，且逗号表示该行下一格，\n表示下一行
pic('../../../Pictures/StellarPlayer/Screenshots/Screenshot 2025-10-16 at 22.42.36.png','./picture.jpg')
