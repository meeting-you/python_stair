# 导入httplib包
import httplib2

# 连接服务器
conn = httplib2.HTTPSConnectionWithTimeout('www.baidu.com')

# 发送HTTP协议GET请求
conn.request('GET', '/')

# 获取结果（结果类型为httplib.HTTPResponse）
result = conn.getresponse()

# 获取HTTP请求结果值，200
# 为成功，具体其他值含义请查看HTTP协议内容
resultStatus = result.status

# 获取请求到的结果内容
resultContent = result.read()
print(resultContent)
# 关闭连接
conn.close()
# 如果要模拟客户端进行请求，还可以在发送请求的时候携带头数据（HTTP
# header）

headers = {"Content-Type": "text/html; charset=gb2312"}
conn.request('POST', '/', headers=headers)

# 除了头数据，还可以在POST的时候带请求参数

# params = urllib.urlencode({'pname': 'pvalue'});
# conn.request('POST', '/', body=params)