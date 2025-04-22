# 특정 조건에 맞는 숫자 찾기

# 정수 n이 주어졌을 때, 1부터 n까지 숫자 중에서 3의 배수 이면서 2의 배수가 아닌 수들만 리스트에 담아 반환하는 함수 작성.

def FindNum(num):
    sortedNums = [] # 반환된 숫자를 저장할 리스트
    for i in range(1,num+1):
        if i % 3 == 0 and i % 2 != 0: # 3의 배수 이면서 2의 배수가 아님
            sortedNums.append(i)
    
    return sortedNums

input_num = int(input("정수 N을 입력하세요: "))
print(FindNum(input_num))
