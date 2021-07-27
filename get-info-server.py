import requests,json

#website 1
file=requests.get('http://khuong.xyz/my-info.php').text 
ip=json.loads(file)['ip']
useragent=json.loads(file)['useragent']

#website 2
file_2=requests.get('http://phukhuong.000webhostapp.com/my-info.php').text
ip=json.loads(file_2)['ip']
useragent=json.loads(file_2)['useragent']
