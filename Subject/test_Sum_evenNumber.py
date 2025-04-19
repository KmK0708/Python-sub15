# 짝수의 합
# 사용자가 자연수 n을 입력하고 1부터 n까지의 짝수 합을 구해라.
# n은 1보다 크고 10000보다 작아야한다.

user_input = int(input("자연수 n을 입력하세요 : "))
answer = 0

for i in range(user_input + 1):
    print(i)
    if i % 2 == 0:
        answer += i

print(f"1 부터 n까지 짝수의 합은 {answer} 입니다.")