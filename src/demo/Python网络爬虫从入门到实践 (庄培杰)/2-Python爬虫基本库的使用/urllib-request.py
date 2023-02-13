import urllib.request

resp = urllib.request.urlopen("http://www.baidu.com")

print("url :", resp.geturl())
print("msg : ", resp.msg)
print("status :", resp.status)
print("resp.version：", resp.version)
print("resp.reason：", resp.reason)
print("resp.debuglevel：", resp.debuglevel)
print("resp.getheaders：", resp.getheaders()[0:2])
print(resp.read().decode('utf-8'))
