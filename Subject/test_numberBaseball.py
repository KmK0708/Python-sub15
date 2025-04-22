# 숫자야구 게임
import random
# (사람 대 컴퓨터로 하는 경우)
# 1. 무작위의 세 자리의 자연수를 만듭니다. ( 000 ~ 999 의 숫자)
nums = list(range(10)) # 0부터 9까지 숫자 리스트
random.shuffle(nums) # 무작위 섞고
answer = nums[:3] # 3개뽑기
trygame = 0 # 시도횟수 변수
print(answer)
# 2. 문제를 맞추는 사람이 세 자리의 수를 얘기합니다.
while True: # 맞출때 까지...
    trygame += 1 #시도 횟수 증가
    strike = 0
    ball = 0
    guess_answer = input("정답을 맞추세요.(예:123): ") # 사용자로부터 입력받음
    guess_list = [int(x) for x in guess_answer] # 입력받은 값을 정수화 시켜 리스트로 만들기 그래야 비교가능
    if len(guess_answer) != 3:
        print("세자리 숫자를 입력하세요")
        continue
    elif not guess_answer.isdigit():
        print("숫자를 입력하세요.")
        continue

    for i in range(3): 
        if guess_list[i] == answer[i]:       # 위치와 숫자 둘 다 맞음
            strike += 1 # 스트라이크 추가
        elif guess_list[i] in answer:        # 숫자만 맞고 위치는 다름
            ball += 1 # 볼 추가

    out = 3 - (strike + ball)  # 나머지는 Out 처리

    #결과 출력
    print(f"결과: {strike} Strike, {ball} Ball, {out} Out")

    #정답일 경우 게임 종료
    if strike == 3:
        print(f"정답! {trygame}번 만에 맞췄어요!")
        break


# 3. 숫자만 맞추고 자릿수는 맞지 않는 경우 Ball, 숫자와 자릿수까지 맞으면 Strike,
#   숫자와 자릿수까지 다 틀린 경우 Out이라고 표시하도록 합니다.
