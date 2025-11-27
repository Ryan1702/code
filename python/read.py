def r():
    a=open('test.txt','r',encoding='utf-8')
    # r -> 只读，指针在开头，文件必须已经创建好了
    # rb -> r+二进制
    # w -> 覆盖写，文档不存在就创建
    # wb -> w+二进制
    # a -> 若无该文件则新建，若有就将输出加在后面
    # a -> 若有该文件则继续输入
    # + -> 可以新增读写功能，w+ = r+
    b=a.read()
    a.close()
    print(b,type(b))
def r1(filename):
    a=open(filename,'w+',encoding='utf-8')
    a.write('吴悠凡\n翁谢童\nwyf\nwxt')
    a.seek(3) # 数字代表的是在从头开始的第几个字节处，一个汉字占一个字符/三个字节
    s=a.read(1) # 读两个字符，如果不加数字，则是全文读取
    ss=a.readline() # 读一行带着末尾换行,也可以加需要读取几个字符
    sss=a.readlines() # 一行一个字符串元素，组成一个列表
    print(s,ss,sss)
if __name__=='__main__':
    r1('try.txt')