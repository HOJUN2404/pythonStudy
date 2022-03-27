# section 13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

words = [] # 영어단어 리스트 1000개 로드

# 게임시도 횟수
n = 1 
# 정답 개수
cor_cnt = 0

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# 리스트 words 확인
# print(words)

input("Ready ? Press Enter Key!")  # Enter Game Start !
start = time.time()


while n <= 5 :
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("* Question # {}".format(n))
    print(q)  # 문제 출력

    x = input()  # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip(): # 입력확인(공백제거)
        print("Pass!")
        cor_cnt +=1
    else:
        print("Wrong!")

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")


print("게임시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작지점
if __name__ == '__main__':
    pass

# print("수행시간 : '%d'" % et)






