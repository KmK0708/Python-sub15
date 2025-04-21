#여러 개의 단어로 이루어진 배열이 주어집니다.
#또한 slices 라는 배열이 주어 집니다.
#각 단어에서 특정 구간(부분 문자열)을 잘라 조합하여
# "polytech"가 나오도록 코드를 짜보시오

# 보니까 slice는 word 배열 자를 부분 지정 해둔것같다.
# apocalypse 의 1번 , 2번 문자 인덱스 p o / 5,6 번 문자 인덱스 l y
# meteorology 의 2,3번 문자 인덱스 t,e ... 각각 인덱스 에 위치한 문자를 가져오면 polytech 완성됨.
def hidden_word (words, slices):
    answer = "" # 답 저장할 변수
    for i in range(len(words)):
        print(i)
        word = words[i] # 현재 단어
        slice_word = slices[i] #

        for start,end in slice_word:
            answer += word[start:end+1]
    return answer

words = ["apocalypse","meteorology","architect","cheetah"]
slices = [[(1, 2), (5, 6)],[(2, 3)],[(2, 2)],[(1, 1)]]

print(hidden_word(words,slices))
