# chapter 06_02
# 흐름제어, 병행처리(Concurrency)
# yeild
# 코루틴(Coroutine)

# yield : 메인루틴 <-> 서브 루틴
# 코루틴제어, 코루틴상태, 양방향 값 전송
# yield from

# 코루틴 : 코루틴 스케쥴링 오버헤드 매우 적다..? 
# 서브루틴 : 메인루틴에서 -> 리턴에 의해 호출 부분으로 돌아와 다시 프로세스
# 코루틴 : 루틴 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 -> 다시 원래 위치로 돌아와 수행 기능 -> 동시성 프로그리맹 기능
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> 공유되는 자원 -> 교착상태 발생 가능성, 컨텍스트 스위칭 비용 발생

# 코루틴 예제1

from calendar import c


def coroutine1():
    print('>>> coroutine started !')
    i = yield
    print('>>> coroutine received : {}'.format(i))


# 제네레이터 선언

c1 = coroutine1()

# print('ex1-1 :', c1, type(c1))

# next(c1)

# 기본으로 None 전달
# next(c1)

# c1.send(100)


# 잘못된 사용

c2 = coroutine1()


# c2.send(100)  예외발생

# 코루틴 예제2
# GEN_CREATED : 처음 대기상태
# GEN_RUNNING : 실행상태
# GEN_SUSPENDED : yield 대기상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine recieved : {}'.format(y))
    z = yield x + y
    print('>>> coroutine recieved : {}'.format(z))


c3 = coroutine2(10)

from inspect import getgeneratorstate

print('ex1-2 :', getgeneratorstate(c3))

print(next(c3))

print('ex1-3 :', getgeneratorstate(c3))

print(c3.send(15))

# print(c3.send(20))    예외

print()
print()
print()

# 데코레이터 패턴

from functools import wraps

def coroutine(func):
    '''Decorator run until yield'''
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer



@coroutine
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term


su = sumer()

print('ex2-1 :', su.send(100))
print('ex2-2 :', su.send(40))
print('ex2-3 :', su.send(60))



















