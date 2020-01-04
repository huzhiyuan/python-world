import os
import time

import requests

# 可以容忍的访问速度,单位:秒
connect_speed_second = 0.18
wifi_name = "saber"

def test():
	while True:
		# auto_connect("saber")
		speed_ok = test_connect_baidu()
		if(speed_ok):
			continue
		else:
			restart_wifi()

		time.sleep(10) #每10s检查一次

def test_connect_baidu():
	try:
		r = requests.get("https://www.baidu.com")
		total_seconds = r.elapsed.total_seconds()
		if total_seconds < connect_speed_second:
			print("网速正常...")
			return True
		else:
			print("网速变慢...")
			return False
	except Exception as e:
		print("访问百度出错!",e)
		return False


def restart_wifi():
	print("重启wifi...")
	cmd = "netsh wlan disconnect"
	os.system(cmd)
	time.sleep(3)  #休眠一会,保证wifi重启完成

	cmd = "netsh wlan connect name={}".format(wifi_name)
	os.system(cmd)
	time.sleep(3)  #休眠一会,保证wifi重启完成


if __name__ == "__main__":
	test()
