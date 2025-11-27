import json

from wxt import file

l=[[[1,2],[3,4]],[[5,6],[7,8]]]
s=json.dumps(l,ensure_ascii=False,indent=3) # list -> str
print(s)
s=json.loads(s)
print(s)
with open('bala.txt','w') as f:
    json.dump(l,f,ensure_ascii=False,indent=3)
with open('bala.txt','r') as f:
    l=json.load(f)
    print(l)