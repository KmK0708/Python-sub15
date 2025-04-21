# 신용카드 번호 만들기

# 다음 조건에 맞게 카드 번호 생성
# 1. 숫자 4,5 또는 6으로 시작
# 2. 총 16자리 숫자여야함.
# 3. 숫자로만 구성되야함.
# 4. 4자리씩 하이픈으로만 나누어야함( - ) 다른 기호 불가능.
# 5. 같은 숫자 4번이상 반복 불가.

# 입력:1. 첫번째줄 : 입력 받을 카드 번호의 개수 n(1이상) 아마 4 입력하면 4개의 카드번호 출력? 랜덤하게..
#     2. 다음 n 줄 : 각각 신용카드 번호 주어짐.

# 출력: 각줄마다 해당 카드 번호 유효하면 vaild 아니면 invaild 위 조건 검사하기.

# 카드 번호 유효성 판별 함수
def isvaildCard(cardnum):
    # 하이픈으로 파트 나누기
    parts = cardnum.split('-')

    if len(parts) != 4: # 파트가 4개가 아니면 유효 하지 않음
        print("길이가 부족합니다.")
        return False # 4123-2399-3929 이면 False
    
    # 파트들 검사돌려서 4자리가 아니고 숫자가 아니면 거부하기.
    for part in parts:
        if len(part) != 4:
            print("카드 부분 번호가 유효하지 않는 길이입니다.")
            return False # 길이가 4자리가 아닐시 false
        if not part.isdigit():
            print("숫자 이외의 문자가 들어가있습니다.")
            return False # 숫자이외면 false 
        
    #카드 넘버 16자리 4개 파트 모음
    cardnumbers = parts[0]+parts[1]+parts[2]+parts[3]

    #첫 카드 넘버가 4,5,6,이 아니면 false
    if cardnumbers[0] not in ['4','5','6']:
        print("유효하지 않는 앞자리입니다.")
        return False
    
    count_SameNum = 1
    for i in range(1,16):
        if cardnumbers[i] == cardnumbers[i-1]: # i자리 수가 그 전자리 수와 같으면
            count_SameNum += 1 # 중복카운트 1증가

            if count_SameNum == 4:
                print("숫자4개가 연속 중복됩니다.")
                return False # 카운트가 4개 (중복4개)
            else:
                count_SameNum = 1 # 초기화

    return True

input_cardnum = int(input("검사할 카드 번호 갯수 입력 : "))

for i in range(input_cardnum):
    card = input(f"{i+1}번째 카드 번호 입력 (예: 4123-4567-8912-3456): ")
    if isvaildCard(card):
        print("Valid")
    else:
        print("Invalid")
