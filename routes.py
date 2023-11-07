# import requests
# import os
# from bardapi import Bard, SESSION_HEADERS


# session = requests.Session()
# session.cookies.set("__Secure-1PSID", "cwjjDkVd1E4HuqXzVJZ4-h6ZCuD0qmfGfkh7yI5-SHG8X9X-SP7Fy8VKCYCEj3qur3wZiA.")
# session.cookies.set( "__Secure-1PSIDCC", "ACA-OxOaNEOIJw4HaCt-4nciS5uAhXluA_vO_U2CRPLYHduhZbGk1T1WXUb6msBoqnlW2XmI1Q")
# session.cookies.set("__Secure-1PSIDTS", "sidts-CjIBNiGH7p63KDJmWpgR5L-GGMZJ36kVt-PEIKn5vq69lKo6JZO6mb_nGlF9xIGUwLE-aRAA")
# # session.headers = SESSION_HEADERS
# session.headers = {
#     "Host": "bard.google.com",
#     "X-Same-Domain": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
#     "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#     "Origin": "https://bard.google.com",
#     "Referer": "https://bard.google.com/",
# }


# # auto
# def generate_response_from_bard(user_content):
#   print('generate_response_from_bard() 호출됨')

#   try:
#     bard = Bard(token_from_browser=True)
#     response = bard.get_answer(user_content)['content']
#     return response
#   except Exception as e:
#     print("토큰 오토값 에러 발생: ", str(e))
#     return "쿠키 값이 잘못되었습니다."

# def generate_response_from_bard(user_content):
#   print('generate_response_from_bard() 호출됨')
#   try:
#     # https://bard.google.com/ 에 로그인하여 쿠키 __Secure-1PSID 의 value값을 아래에 붙여넣기
#     token = 'cwjjDv6cqXbpl3xojnbsXBOoOeZ9o1yj24V7U-VlDyCOAVFYEOE1O5Mow6KFMT3QhyjXrQ.' 
#     print("token: ", token)
#     bard = Bard(token=token)
#     response = bard.get_answer(user_content)['content']
#     return response
#   except Exception as e:
#     print("토큰 직접사용 에러 발생: ", str(e))
    
#     try:
#       bard = Bard(token_from_browser=True)
#       response = bard.get_answer(user_content)['content']
#       return response
#     except Exception as e:
#       print("브라우저 쿠키를 사용한 예외 발생: ", str(e))
#       return "쿠키값이 잘못되었습니다."

from bardapi import Bard
from bardapi import BardCookies
import os
import requests
os.environ['_BARD_API_KEY'] = 'cwjjDi-zC6Qwc3k3ftT0tFFSbpHlLhPJF700oNHbfqMFXskW5DKTUWxoaTHZX0X-7p7opA.'
token='cwjjDi-zC6Qwc3k3ftT0tFFSbpHlLhPJF700oNHbfqMFXskW5DKTUWxoaTHZX0X-7p7opA.'

cookie_dict = {
    "__Secure-1PSID": "cwjjDi-zC6Qwc3k3ftT0tFFSbpHlLhPJF700oNHbfqMFXskW5DKTUWxoaTHZX0X-7p7opA.",
    "__Secure-1PAPISID": "BQdEfnLMOY_mN5P_/A7gB-vXnYKwwXZKrR",
    "__Secure-1PSIDCC": "ACA-OxPnX-zp18HGNYDe22Zy51kdJf7T8vmpGGVSc8aTHzaFC2y2syKMH_jmYIiJ2efQxeK4_Q",
    # Any cookie values you want to pass session object.
}



bard = BardCookies(cookie_dict=cookie_dict)

# session = requests.Session()
# session.headers = {
#             "Host": "bard.google.com",
#             "X-Same-Domain": "1",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
#             "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#             "Origin": "https://bard.google.com",
#             "Referer": "https://bard.google.com/",
#         }

# session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
# # session.cookies.set("__Secure-1PSID", token) 
# bard = Bard(token=token, session=session, timeout=30)

def generate_response_from_bard(user_content):
  print('generate_response_from_bard() 호출됨')
  print('요청---', user_content)
  try:    
    response = []
    response.append(bard.get_answer(user_content)['content'])

    

    
    # new_user_content = f"{response[0]}에 따라 어떤 행동을 취해야하는지도 알려줘"
    # print('요청---', new_user_content)
    # response.append(bard.get_answer(new_user_content)['content'])

    print(response)
    return response
  except Exception as e:
    print("브라우저 쿠키를 사용한 예외 발생: ", str(e))
    return "쿠키값이 잘못되었습니다."