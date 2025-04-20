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
        return False # 4123-2399-3929 이면 False
    
    # 파트들 검사돌려서 4자리가 아니고 숫자가 아니면 거부하기.
    for part in parts:
        if len(part) != 4:
            return False
        if not part.isdigit():
            return False
        
    #카드 넘버 16자리 4개 파트 모음
    cardnumbers = part[0]+part[1]+part[2]+part[3]


