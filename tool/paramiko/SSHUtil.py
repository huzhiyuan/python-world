#-*- coding:utf-8 -*-

import paramiko
host = '192.168.158.130'
username='hzy'
password = 'xxx'

def test():
    test_transport()

def test_transport():
    '''执行多个命令'''
    transport = paramiko.Transport((host, 22))
    transport.connect(username=username, password=password)
    # 将sshclient的对象的transport指定为以上的transport
    ssh = paramiko.SSHClient()
    ssh._transport = transport

    stdin, stdout, stderr = ssh.exec_command('cd /home/hzy/test/')
    res,err = stdout.read(),stderr.read()
    result = res if res else err
    print(result.decode())
    ssh._transport = transport
    stdin, stdout, stderr = ssh.exec_command('ls')
    res,err = stdout.read(),stderr.read()
    result = res if res else err
    print(result.decode())

    transport.close()


def test_put():
    transport = paramiko.Transport((host, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put( 'Linux.txt','/home/hzy/test/logs/Linux.txt')#将Linux上的/root/Linux.txt下载到本地
    transport.close()

def test_get():
    transport = paramiko.Transport((host, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get('/home/hzy/test/logs/Linux.txt', 'Linux.txt')#将Linux上的/root/Linux.txt下载到本地
    transport.close()

def test_cmd():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command('cd /home/hzy/test/')
    res,err = stdout.read(),stderr.read()
    result = res if res else err
    print(result.decode())

    stdin, stdout, stderr = ssh.exec_command('ls')
    res,err = stdout.read(),stderr.read()
    result = res if res else err
    print(result.decode())
    ssh.close()

if __name__ == '__main__':
    test()


