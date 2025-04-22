#장바구니 할인 계산기

#마트에서 장 볼 때, 어떤 상품은 할인, 어떤건 적용 x
#할인 조건에 따라 지불해야하는 총 금액 계산 프로그램

#-------------------조건-------------------#
# 물건 가격이 10000원 이상이면 10% 할인
# 10000원 미만 이면 할인 x
# 여러 개 샀을 때 최종 지불 금액 계산.
product_prices=[] # 담은 물품 가격 리스트
total = 0 # 총합 변수
while len(product_prices) < 5: # 담은 상품이 5개까지 반복하기
    
    input_price = int(input("구입한 상품의 가격을 입력하세요: "))
    product_prices.append(input_price)
    print(product_prices)

for price in product_prices: # 가격 리스트 순회하기
    if price >= 10000: # 가격이 만원 넘어가면
        price *= 0.9 # 10퍼 할인
    total += int(price) # 정수형으로 변환

print(f"지불해야 할 금액은 {total} 입니다.")