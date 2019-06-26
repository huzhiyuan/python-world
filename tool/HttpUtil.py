import requests

headers = {'content-type':'application/json'}


def test():
    get("http://localhost:8080/global/test?key=xxxxx")


def get(url):
    result = requests.get(url,headers=headers)
    print(result.content)


if __name__ == '__main__':
    test()
