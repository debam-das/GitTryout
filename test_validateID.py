import json
import pytest
import requests
import allure



#method for Get request Ravi 5955
class Test_api:
    def test_getRequest(self):
        res_code = requests.get("https://gorest.co.in/public/v1/users")
        result = json.dumps(res_code.json(), indent=8)
        user_data = res_code.json().get("data")
        print(user_data)
        for element in user_data:
            if element.get("name") == "Kirti Banerjee":
                if element.get("gender") == "female":
                    assert True
                else:
                    assert False


# def test_getRequest():
#     res_code = requests.get("https://gorest.co.in/public/v1/users")
#     result = json.dumps(res_code.json(), indent=8)
#     user_data = res_code.json().get("data")
#
#     for element in user_data:
#         if element.get("name") == "Guru Sethi":
#             # print(element.get("gender"))
#             if element.get("gender") == "male":
#                 assert True
#             else:
#                 assert False
#
#
# test_getRequest()


