import os
import time
from time import strftime

print(os.getcwd())
print(os.listdir())
os.mkdir('daydayup') # ./表示当前路径，./aa/bb/cc表示嵌套文件夹
os.rmdir('daydayup')
os.chdir('..')
print(os.getcwd())
print(os.listdir())
print('-'*40)
for dirs,dirlist,files in os.walk('wxt'):
    print(dirs) # 当前路径
    print(dirlist) # 文件夹
    print(files) # 所有文件
# os.remove(file)
# os.rename(file_pre,file_now)
os.chdir('wxt') # 设置当前目录
ss=os.stat('txt_name.txt') # 获取文件信息
sss=strftime('%Y-%m-%d %H-%M-%S',time.localtime(ss.st_atime)) # 文件最后一次访问时间
ssss=strftime('%Y-%m-%d %H-%M-%S',time.localtime(ss.st_ctime)) # windows -> 创建时间
sssss=strftime('%Y-%m-%d %H-%M-%S',time.localtime(ss.st_mtime)) # 文件最后一次修改时间
print(sss,ssss,sssss,sep='\n')
print(ss.st_size) # 文件大小，单位是字节