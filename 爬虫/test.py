import urllib2

headers = {
	"User-Agent":"Mozilla/5.0 (2Windows NT 10.0; WOW64) AppleWebKit/537.36 (K    HTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

request =  urllib2.Request("http://www.baidu.com/",headers = headers)

response = urllib2.urlopen(request)

print response.read()

http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule 

 
