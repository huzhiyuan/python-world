import base64

f=open(r'C:\github\go\src\go-cook-book\blog\images\go_package_init.jpg','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print(str(ls_f))
