def f():
    s=input()
    a=open('test.txt','a',encoding='utf-8')
    a.write('123')
    a.write('\n')
    a.close()
    b=open('test.txt','a',encoding='utf-8')
    b.write(s) # 只能写字符串
    b.close()
def xie(file,b):
    a=open(file,'a',encoding='utf-8')
    a.writelines(b) # 只能写全部元素均为字符串的列表
    a.close()
if __name__=='__main__':
    lst=['1','2','3','4','5']
    xie('text.txt',lst)