import requests
import json

# / --> Hello
url = 'http://162.55.220.72:5005/'

# resp_hello = requests.get(url)

# # print('resp_hello =', resp_hello.status_code)
#
# resp_hello_headers = resp_hello.headers
# print('headers: ', resp_hello_headers)
# for key, value in resp_hello_headers.items():
#     print('key =', key)
#     print('value = ', value)
#     print('=========================================')

#===========================================================================

# url_first = url +'first'
# resp_first = requests.get(url_first)
# print('resp_first = ', resp_first.text)

#=============================================================================

# end_point_get_method = 'get_method'
# url_get_method = url + end_point_get_method
#
# get_method_params = {'name': 'Anastasiya',
#                      'age': '18'}
# resp_get_method = requests.get(url_get_method, params=get_method_params)
# resp_text = resp_get_method.text
# resp_json = resp_get_method.json()
#
# print('resp_get_method = ', resp_json, type(resp_json))

#==============================================================================

# end_point_user_info_1 = 'user_info_1'
# url_user_info_1 = url + end_point_user_info_1
#
# url_user_info_1_data = {'age': 28,
#                         'name': 'Eldar',
#                         'weight': 90}
#
# res_post_user_info_1 = requests.post(url_user_info_1, data=url_user_info_1_data)
# resp_user_info_1_json = res_post_user_info_1.json()
# print('resp_user_info_1_json =', resp_user_info_1_json)

#=============================================================================

login_endpoint = '/login'
url_login =  url + login_endpoint

login_data = {'login': 'Eldar',
              'password': 34}
res_login = requests.post(url_login, data=login_data)
user_token = res_login.json()['token']
print(user_token)

end_point_user_info = 'user_info'
url_user_info = url + end_point_user_info

user_info_data = {'age': 28,
                  'name': 'Eldar',
                  'salary': 9000,
                  'auth_token': user_token}
json_data = json.dumps(user_info_data)
req_headers = {'Content-type': 'application/json'}

res_post_user_info = requests.post(url_user_info,
                                   data=json_data,
                                   headers=req_headers)
resp_user_info_json = res_post_user_info.json()

print(resp_user_info_json)
for key, value in resp_user_info_json.items():
    print('key =', key)
    print('value = ', value)






