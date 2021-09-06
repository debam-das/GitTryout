import requests
import json

#method for Get request
def getRequest(url,key,value):
    res_code=requests.get(url)
    result=json.dumps(res_code.json(),indent=8)
    user_data=res_code.json().get("data")
    for element in user_data:
        if element.get(key)==value:
            for  ikey in element:
                print(ikey,element.get(ikey))
            print("---------------")

#final Execution
getRequest("https://gorest.co.in/public/v1/users","status","active")