import admin.mine # 自动会运行这个包中的__init__文件，只会运行一次
print(admin.mine.name)
print('-'*40)
from admin import mine as b # 自动运行mine也只会有一次，在第一次import的时候
print(b.name)
print('-'*40)
from admin.mine import name as names
print(names)
import admination
print('-'*40)
print(admination.s)