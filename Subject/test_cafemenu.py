#카페 메뉴 리스트 가격
menu = {"아메리카노": 2500, "카페라떼": 3000,
        "카페모카": 3500,"티라미수": 4000}
orders = []

while True:
  order_input = input("메뉴를 입력하세요(끝내려면 끝 입력) : ")
  
  if order_input == "끝":
    break
  if order_input in menu:
    orders.append(order_input)
  else:
    print("메뉴에 없습니다. 다시 입력해주세요.")

# 총 합계 계산
total = 0
for item in orders:
    total += menu[item]

print("총 결제 금액은", total, "원입니다.")