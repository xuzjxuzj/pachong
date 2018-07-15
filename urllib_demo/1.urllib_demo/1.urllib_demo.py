from urllib import request

# 明确url
base_url = 'http://www.baidu.com'

# 发起一个http请求，返回一个类文件对象
response = request.urlopen(base_url)

# 获取响应内容
abc = response.read().decode('utf-8')

with open('1.baidu.html','w',encoding="utf-8") as f:
    f.write(abc)

'''
使用urllib.request 的 urlopen(),根据url发起一个http请求，返回一个类文件对象
读取返回的内容，通过编码，得到请求的网页源码，保存在文件中。
'''