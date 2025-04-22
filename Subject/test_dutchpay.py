# 더치페이 프로그램
# 김,고,장,백(4명)은 모임에서 식당->바->카페를 갔다.
# 이때, 식당, 바, 카페에서 나온 금액을 각각 입력받고 각자 먹은 만큼 계산할 수 있는 코드를 만든다.
# 각각의 인원은 중간까지만 가거나, 중간에 합류할 수 있다.
# 예시)고와 장은 식당은 가지 않고 바에서 합류했으며, 백과 장은 카페를 가지 않고 먼저 일어났다.

#일단 식당, 바, 카페에서 나온 총 금액을 입력 받는다.
Total_food_price = int(input("식당에서 나온 금액을 입력 하세요 : "))
Total_bar_price = int(input("바에서 나온 금액을 입력 하세요 : "))
Total_cafe_price = int(input("카페에서 나온 금액을 입력 하세요 : "))

Yes = True
No = False

# 그 다음은.. 사람별로 그 장소에 갔는지 안갔는지를 설정한다.
people_inout = {
    "김":{"식당":Yes, "바":Yes, "카페":Yes},
    "고":{"식당":Yes, "바":No, "카페":No},
    "장":{"식당":Yes, "바":Yes, "카페":No},
    "백":{"식당":No, "바":No, "카페":Yes}
}
김 = 0
고 = 0
장 = 0
백 = 0
people = ["김","고","장","백"]
#식당에 간 사람들로 식당 금액 n분의1
# 각 사람을 검사해서 식당에 갔으면 food_people에 추가
food_people = []
for name in people:
    if people_inout[name]["식당"] == True:
        food_people.append(name)

# 식당에 간 사람이 1명 이상이면 계산 진행
if len(food_people) > 0:
    # 1인당 금액 = 총 금액을 인원 수로 나눈 값
    share = Total_food_price // len(food_people)

    # 각 사람 이름에 맞게 금액을 더함
    for name in food_people:
        if name == "김":
            김 += share
        elif name == "고":
            고 += share
        elif name == "장":
            장 += share
        elif name == "백":
            백 += share

# 바 계산
bar_people = []  # 바에 간 사람 저장
for name in people:
    if people_inout[name]["바"] == True:
        bar_people.append(name)

# 바에 간 사람이 있으면 계산 진행
if len(bar_people) > 0:
    share = Total_bar_price // len(bar_people)
    for name in bar_people:
        if name == "김":
            김 += share
        elif name == "고":
            고 += share
        elif name == "장":
            장 += share
        elif name == "백":
            백 += share


# 카페 계산
cafe_people = []  # 카페에 간 사람 저장
for name in people:
    if people_inout[name]["카페"] == True:
        cafe_people.append(name)

# 카페에 간 사람이 있으면 계산 진행
if len(cafe_people) > 0:
    share = Total_cafe_price // len(cafe_people)
    for name in cafe_people:
        if name == "김":
            김 += share
        elif name == "고":
            고 += share
        elif name == "장":
            장 += share
        elif name == "백":
            백 += share

# 결과 출력
print("\n각자 내야 할 금액 ")
print("김 :", 김, "원")  # 김이 내야 할 금액 출력
print("고 :", 고, "원")  # 고가 내야 할 금액 출력
print("장 :", 장, "원")  # 장이 내야 할 금액 출력
print("백 :", 백, "원")  # 백이 내야 할 금액 출력
