import random
random.seed(1314)
print(random.random())
print(random.randint(1,10)) # 闭区间整数
print(random.randrange(1,10,3)) # 左开右闭整数
print(random.uniform(1,10)) # 闭区间小数
l=[i*i for i in range(1,10)]
print(random.choice(l))
print(l)
random.shuffle(l)
print(l)
random.shuffle(l)
print(l)