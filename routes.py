import requests
import json
import re
from readQuestion import readFile


session = requests.Session()
session.headers = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}
session.cookies.set("__Secure-1PSID", "")
session.cookies.set( "__Secure-1PSIDCC", "")
session.cookies.set("__Secure-1PSIDTS", "")

from bardapi import Bard
# from bardapi import BardCookies
# import os
# os.environ['_BARD_API_KEY'] = ''
token=''

# cookie_dict = {
#     "__Secure-1PSID": "",
#     "__Secure-1PAPISID": "",
#     "__Secure-1PSIDCC": "",
# }

bard = Bard(token=token, session=session, timeout=30)

def generate_response_from_bard(user_content, user_facs, user_tags):
  print('generate_response_from_bard() 호출됨')
  print('---user_content:', user_content)
  print('---user_facs:', user_facs)
  print('---user_tags:', user_tags)

  read_file = readFile()
  patternContent = r'이곳에_질문을_작성하세요\.'
  patternFac = r'이곳에_설비를_작성하세요\.'
  patternTag = r'이곳에_태그를_작성하세요\.'

  request_content = re.sub(patternContent, user_content, read_file)
  request_content = re.sub(patternFac, user_facs, request_content)
  request_content = re.sub(patternTag, user_tags, request_content)
  print('---request_content:', request_content)

  try:    
    response = []
    response.append(bard.get_answer(request_content)['content'])

    print(response[0])
    
    # JSON 형식을 추출할 정규식 패턴
    pattern = r'```(.*?)```'
    # print('[1]pattern', pattern)
    # 문자열에서 JSON 부분을 추출
    matches = re.search(pattern, response[0], re.DOTALL)
    # print('[2]matches', matches)

    if matches:
        json_data = matches.group(1)
        print('[3]json_data', json_data)
    else:
        print("JSON 데이터를 찾을 수 없습니다.")

    return json_data
  except Exception as e:
    print("예외 발생: ", str(e))
    return "서버 오류"