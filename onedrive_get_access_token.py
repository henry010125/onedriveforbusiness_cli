import requests
import json
from urllib import parse

tenant_ID = '78e51081-e8e0-4b26-915d-fafa3c43023c'
client_id = '486ef416-2ffc-42eb-8dd0-83e59b59bd8b'
client_secret = 'ste7Q~617UmBomw8LEJzMxZV55.wBe06OFly5'

url = 'https://login.microsoftonline.com/'+tenant_ID+'/oauth2/v2.0/authorize?client_id='+client_id+'&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A4452%2F&response_mode=query&scope=https%3A%2F%2Fgraph.microsoft.com%2FFiles.ReadWrite'
print('打開下列網址：'+url)
print('輸入登入後顯示的網址：',end='')
redirect_url = input()
code = redirect_url.split('&')[0].split('=')[1]

HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
url = 'https://login.microsoftonline.com/'+tenant_ID+'/oauth2/v2.0/token'
FormData = {'client_id':client_id,'scope':'https://graph.microsoft.com/Files.ReadWrite offline_access','redirect_uri':'http://localhost:4452/','client_secret':client_secret,'grant_type':'authorization_code','code':code}
data = parse.urlencode(FormData)
retur = json.loads(requests.post(url=url, headers=HEADERS, data=data).text)
token = retur['access_token']
print('你的訪問令牌為：'+token)
refresh_token = retur['refresh_token']
print('你的刷新令牌為：'+refresh_token)