import random
import os
import json

# 🎳 볼링 점수 계산 게임 클래스
class BowlingGame:
    def __init__(self):
        # 게임 관련 변수 초기화
        self.total_score = 0  # 누적 점수
        self.Maxscore = 300  # 최대 점수 (볼링은 300점 만점)
        self.MaxbowlingFrame = 10  # 총 프레임 수
        self.strike = 10  # 스트라이크 기준 핀 수
        self.chance = 2  # 각 프레임당 최대 투구 기회
        self.totalsave_score_list = []  # 각 프레임 점수 기록
        self.startpins = 10  # 초기 핀 개수
        self.Isrunning = True  # 게임 진행 여부
        self.bowlingFrame = 1  # 현재 프레임 번호

    # ✅ 누적 점수 계산 함수
    def calculate_total_score(self):
        total = 0  # 점수 합산 변수
        frames = self.totalsave_score_list  # 프레임 기록 참조

        for i in range(len(frames)):
            frame = frames[i]

            # 🎯 스트라이크 처리: 다음 두 투구의 점수 보너스
            if frame == [10]:
                if i + 1 < len(frames):
                    next1 = frames[i + 1]
                    if next1 == [10] and i + 2 < len(frames):
                        next2 = frames[i + 2]
                        bonus = 10 + next2[0]
                    elif next1 == [10]:
                        bonus = 10
                    else:
                        bonus = sum(next1)
                    total += 10 + bonus
                else:
                    total += 10  # 마지막 스트라이크일 경우

            # 🎳 스페어 처리: 다음 한 투구 점수 보너스
            elif len(frame) == 2 and sum(frame) == 10:
                if i + 1 < len(frames):
                    next1 = frames[i + 1]
                    bonus = next1[0]
                    total += 10 + bonus
                else:
                    total += 10

            # 일반 프레임: 단순 합산
            else:
                total += sum(frame)

        return total  # 누적 점수 반환

    # 🎮 실제 게임 진행 함수
    def play(self):
        # 10프레임까지 루프
        while self.bowlingFrame <= self.MaxbowlingFrame and self.Isrunning:
            print(f"\n현재 프레임은 {self.bowlingFrame} 프레임 입니다.")

            for a in range(self.chance):
                isTry = input("공을 굴리겠습니까? 1.네 2.아니오 : ")
                if isTry == "1":
                    if a == 0:
                        # 첫 투구: 0~10 중 랜덤
                        first_hit = random.randint(0, 10)
                        print("\n첫번째 굴린 결과", first_hit, "이 나왔습니다.")
                        if first_hit == self.strike:
                            print("스트라이크!!")
                            self.totalsave_score_list.append([10])
                            self.bowlingFrame += 1
                            break
                        else:
                            remainpins1 = 10 - first_hit
                            print("\n현재 남은 핀 : ", remainpins1)
                    else:
                        # 두 번째 투구: 남은 핀 수 안에서 랜덤
                        second_hit = random.randint(0, remainpins1)
                        print("\n두 번째 투구 결과 : ", second_hit)
                        remainpins2 = remainpins1 - second_hit
                        print("현재 남은 핀 : ", remainpins2)

                        # 스페어 판정
                        if a != 0 and first_hit + second_hit == 10:
                            print("스페어!")

                        # 프레임 점수 기록
                        total_frame_score = [first_hit, second_hit]
                        self.totalsave_score_list.append(total_frame_score)
                        self.bowlingFrame += 1
                        break
                else:
                    print("\n굴리기를 취소하셨습니다.")
                    self.Isrunning = False
                    break

        # 게임 종료 후 출력
        print("볼링 종료!!")
        print("프레임별 점수:", self.totalsave_score_list)
        print("총 점수는:", self.calculate_total_score(), "점입니다.")
