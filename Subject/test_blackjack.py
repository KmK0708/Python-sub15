#블랙잭 게임
# 두명이상 플레이어 (딜러 포함)
# 카드받고 가진 카드 합을 기준
# hit ,stay/stand, doubledown, split
# 카드의 합이 21을 초과한 경우 bust (패배)
# blackjack A + 10,k,j,q 로 21을 이루면 게임 종료 (승리)
# 딜러는 17점 이상일 때 무조건 stay 합니다.

import random

#카드 덱 생성
def make_deck():
    #일반적인 포커 덱은 52장 이 구성되어있다.
    #카드 리스트
    card = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    #카드 덱 52장 위 card 4개의 합이 1개의 덱 (클로버,다이아,하트,스페이드)
    decks = card * 4 * 4
    #블랙잭은 52장 * 4개의 덱을 쓴다.
    #덱 섞기
    random.shuffle(decks)
    return decks

#카드 뽑기
def Drawcard(decks):
    return decks.pop()

#점수계산
def calc_blackjack_score(cards):
    score = 0 # 점수
    A_count = 0 #A 가 몇개있나 확인하기
    
    #가진 카드들에 j,q,k,10 확인
    for card in cards:
        if card in ['10','J','Q','K']:
            #있으면 10점
            score += 10
        elif card == 'A':  # 뽑은 카드가 a면
            A_count += 1 # 에이스 갯수 추가
            score += 11 # 점수 11점 
        else:
            # 나머지 숫자카드이면 그것대로 점수추가하기
            score += int(card)
    # 점수가 21점 미만이고 A가 있을때 점수 계산
    while score > 21 and A_count:
        score -= 10
        A_count -= 1
    
    return score

#플레이어 게임
def playerGame(name,cards,deck):
    print(f"\n▶ {name}의 차례 시작")
    while True:
        score = calc_blackjack_score(cards)
        print(f"{name}의 현재 카드: {cards}, 총합: {score}")

        if score > 21:
            print(">> BUST! (21 초과)")
            break
        elif score == 21:
            print(">> BLACKJACK!")
            break
        else:
            # 초보자용: 17 이상이면 자동으로 스탠드
            if score >= 17:
                print(">> STAY")
                break
            else:
                print(">> HIT (카드 추가)")
                cards.append(Drawcard(deck))

 # 최종 결과 판단 함수
def print_result(player_name, player_cards, dealer_cards):
    #플레이어 점수
    player_score = calc_blackjack_score(player_cards)
    #딜러 점수
    dealer_score = calc_blackjack_score(dealer_cards)

    print(f"\n {player_name} : {player_cards}, 총합: {player_score}")
    print(f" 딜러 : {dealer_cards}, 총합: {dealer_score}")

    if player_score > 21:
        result = "LOSE"
    elif dealer_score > 21:
        result = "WIN"
    elif player_score > dealer_score:
        result = "WIN"
    elif player_score == dealer_score:
        result = "DRAW"
    else:
        result = "LOSE"

    print(f"🎲 결과 : {result}")

deck = make_deck()

# 딜러: 카드 2장 (1장은 숨김)
dealer = [Drawcard(deck), Drawcard(deck)]

# 플레이어: 카드 2장
player = [Drawcard(deck), Drawcard(deck)]

# 오픈 상태 보여주기
print(f"딜러의 오픈 카드: {dealer[0]}")
print(f"플레이어의 카드: {player}")

# 플레이어 차례
playerGame("플레이어", player, deck)

# 딜러 차례 (조건: 17 이상일 때 스탠드)
print("\n▶ 딜러 차례 시작")
while calc_blackjack_score(dealer) < 17:
    dealer.append(Drawcard(deck))

# 최종 결과 출력
print_result("플레이어", player, dealer)