from bardapi import Bard

def generate_response_from_bard(user_content):
  print('generate_response_from_bard() 호출됨')

  # https://bard.google.com/ 에 로그인하여 쿠키 __Secure-1PSID 의 value값을 아래에 붙여넣기
  token = 'cwjjDmFGsUIqywL0RTdVUFA4d7DWBaduAOJt91ZCyHvXocer5XzdIgA0HhgZA5AV5aHXMQ.' 
  bard = Bard(token=token)
  response = bard.get_answer(user_content)['content']

  print(response)
  return response