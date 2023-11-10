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
session.cookies.set("__Secure-1PSID", "dAjjDkebAXZJEa3k9B__u2-M9qUhK-O8AyvtUb46JY-rZleQ5Azx-e3zaeDyf_oo_jvP_A.")
session.cookies.set( "__Secure-1PSIDCC", "ACA-OxPBScT607OuMi87idW_ImKMhLi-PrZFuspGWWsmHvrIuKMvnbF7NYxI-ixBV1_G-L11fw")
session.cookies.set("__Secure-1PSIDTS", "sidts-CjEBNiGH7jldZYQHcbNv0G_NBVDqwsy_I5Z1UnH6_ppgD2zrcNmVJDsp8vrC_0QemlOUEAA")

from bardapi import Bard
# from bardapi import BardCookies
# import os
# os.environ['_BARD_API_KEY'] = ''
token='dAjjDkebAXZJEa3k9B__u2-M9qUhK-O8AyvtUb46JY-rZleQ5Azx-e3zaeDyf_oo_jvP_A.'

# cookie_dict = {
#     "__Secure-1PSID": "",
#     "__Secure-1PAPISID": "",
#     "__Secure-1PSIDCC": "",
# }

bard = Bard(token=token, session=session, timeout=30)

def generate_response_from_bard(user_content):
  print('generate_response_from_bard() 호출됨')
  print('---user_content:', user_content)

  read_file = readFile()
  pattern = r'이곳에_질문을_작성하세요\.'

  request_content = re.sub(pattern, user_content, read_file)
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

        # # JSON을 파싱
        # try:
        #     data = json.loads(json_data)
        #     print(json.dumps(data, indent=2))  # JSON을 예쁘게 출력
        # except json.JSONDecodeError as e:
        #     print("JSON 파싱 오류:", e)
    else:
        print("JSON 데이터를 찾을 수 없습니다.")


    # # 정규식 패턴
    # pattern = r'```(.*?)```'

    # # 문자열에서 패턴에 맞는 데이터 추출
    # matches = re.search(pattern, response[0])

    # if matches:
    #     extracted_data = matches.group(1)
    #     print('extracted_data[0]',extracted_data)
    # else:
    #     print("추출할 데이터를 찾을 수 없습니다.")

    # # JSON 문자열 정리 (줄바꿈 문자와 띄어쓰기 제거)
    # cleaned_json = extracted_data.replace('\n', '').replace(' ', '')
    # print('cleaned_json[1]',cleaned_json)

    # # JSON 문자열 추출
    # start_index = cleaned_json.find('{')  # JSON 시작 지점 찾기
    # print('start_index[2]',start_index) 
    # if start_index != -1:
    #     json_string = cleaned_json[start_index:]
    #     print('json_string[3]',json_string)
    #     try:
    #         json_data = json.loads(json_string)
    #         print(json.dumps(json_data, indent=2))  # JSON을 예쁘게 출력
    #     except json.JSONDecodeError:
    #         print("주어진 문자열에서 유효한 JSON 형식을 찾을 수 없습니다.")
    # else:
    #     print("JSON 시작 지점을 찾을 수 없습니다.")

    return json_data
  except Exception as e:
    print("예외 발생: ", str(e))
    return "서버 오류"