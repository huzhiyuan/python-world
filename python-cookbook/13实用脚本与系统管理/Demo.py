
#终止程序并显示错误信息
for i in range(1,10):
 if i>3:
     raise SystemExit('it failed!')
 else:
     print(i)
