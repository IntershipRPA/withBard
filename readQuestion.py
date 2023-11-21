def readFile():
  # 파일 열기
  file_path = './question.txt'
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      # 파일 내용 읽기
      file_contents = file.read()
      # print("파일 내용:")
      # print(file_contents)
      return file_contents
  except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")


