# 사용자가 입력한 비밀번호의 강도를 검사하는 프로그램 작성
# 강도 평가는 여러 조건을 기준으로 점수 부여, 점수에 따라 '강함' '보통' '약함' 으로 구분
# 사용자로 부터 입력받기 input()

# 암호 길이 확인 함수
def ispwLong (input_pw):
    # 암호가 8자리 이상이면
    if len(input_pw) >= 8:
        return 2 # 2점 반환
    else:
        return 0

# 암호 숫자 포함 판별 함수
def pwinNumber(input_pw):
    for ch in input_pw: # for문으로 한글자씩 반복하기
        if ch.isdigit(): #isdigit으로 숫자있는지 보기
            return 2 # 있으면 2점
    return 0
        
# 대문자 포함 확인 함수
def intoUpper(input_pw):
    for ch in input_pw:
        if ch.isupper():
            return 1
    return 0


# 소문자 포함 확인 함수
def intoLower(input_pw):
    for ch in input_pw:
        if ch.islower():
            return 1
    return 0

def checking_pw(input_pw):
  # 점수 변수
  score = 0
  # 길이 확인
  long_score = ispwLong(input_pw)
  score += long_score
  if long_score != 0:
      print("[O] 길이 8자 이상")
  else:
      print("[X] 길이 8자 이상")

  # 숫자 포함 여부 확인
  num_score = pwinNumber(input_pw)
  score += num_score
  if num_score != 0:
      print("[O] 숫자 포함")
  else:
      print("[X] 숫자 포함")

  # 대문자 포함 여부 확인
  upper_score = intoUpper(input_pw)
  score += upper_score
  if upper_score != 0:
      print("[O] 대문자 포함")
  else:
      print("[X] 대문자 포함")
  # 소문자 포함 여부 확인
  lower_score = intoLower(input_pw)
  score += lower_score
  if lower_score != 0:
      print("[O] 소문자 포함")
  else:
      print("[X] 소문자 포함")

  # 최종 점수 출력
  print(f"\n점수는 {score} 입니다.")

  # 점수에 따라 강도 분류
  if score >= 6:
      print("비밀번호 강도: 강함")
  elif score >= 4:
      print("비밀번호 강도: 보통")
  else:
      print("비밀번호 강도: 약함")

password = input("암호를 입력하세요 : ")

checking_pw(password)

# 조건 검사 해서 점수 부여
# 비밀번호 길이 8자 이상 2점 부여
# 숫자 하나 이상 포함 2점 부여
# 대문자 포함 1점
# 소문자 포함 1점
# 각 조건 함수로 검사 , 점수와 피드백 메세지 반환
# 모든 조건 검사 후 총점 계산, 다음 기준으로 보안 강도 출력
# 6점이상 강도: 강함
# ~4점이상 강도 : 중간
# 3점 이하 강도 : 약함

# 각 조건별 평가 메세지 출력 (예:  O 숫자 포함 , X 대문자 없음)
