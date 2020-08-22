import requests #html SourceCode
import json,os
'''
source=requests.get('address')
result=source.text
result=json.loads(result)
for i in result:
    print(i['userId'])
'''

sourceweb='https://jsonplaceholder.typicode.com/todos'
source=requests.get(sourceweb)
#<Response [200]>
result=source.text
print(type(result))#<class 'str'>
result=json.loads(result)
print(result[0])
for i in result:
    if i['userId']==1:
        print(i['title'])
'''
for i in result:
    print(i['id'])
'''


