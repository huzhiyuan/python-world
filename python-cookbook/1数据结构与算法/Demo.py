print('1.1 将序列分解为单独的变量')
p=(3,4)
x,y=p
print(x)
print(y)

print('1.2 从任意长度分解对象')
record=('dive','1111@qq.com','123','231','132')
name,email,*phones=record
print(name)
print(email)
print(phones)
