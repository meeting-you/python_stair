
# document：https://docs.python.org/zh-cn/3/library/http.html

import http.client

conn1 = http.client.HTTPConnection('www.baidu.com')
response = conn1.getresponse()
print(response.msg, response.status)