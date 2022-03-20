# Section02-2
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print("My name is Hojun")

# 변수 선언
myName = "호준"
print(myName)

# 조건문
if myName == "호준":
    print("ok")

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i,j), i*j)


# 함수
def function1():
    print("함수1 실행")

function1();

# 클래스 생성
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
