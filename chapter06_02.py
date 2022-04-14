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


# 코루틴 예제3 (예외처리)
class SampleException(Exception):
    '''설명에 사용할 예외 유형'''


def coroutine_except():
    print('>> coroutine started')
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print('-> SampleException handled. Continuing..')
            else:
                print('-> coroutine received : {}'.format(x))
    finally:
        print('-> coroutine ending')


exe_co = coroutine_except()

print('ex3-1 :', next(exe_co))
print('ex3-2 :', exe_co.send(10))
print('ex3-3 :', exe_co.send(100))
print('ex3-4 :', exe_co.throw(SampleException))
print('ex3-5 :', exe_co.send(1000))
print('ex3-6 :', exe_co.close())

print()
print()

# 코루틴 예제4 (Return)

def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total / cnt
    return 'Average : {}'.format(avg)


avger2 = averager_re()

next(avger2)

avger2.send(10)
avger2.send(30)
avger2.send(50)

try:
    avger2.send(None)
except StopIteration as e:
    print('ex4-1 :', e.value)



# 코루틴 예제 5 (yield from)
# StopIteration 자동 처리 (3.7 이상 버전에서는 await)
# 중첩 코루틴 처리

def gen1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = gen1()

print('ex5-1 :', next(t1))
print('ex5-2 :', next(t1))
print('ex5-3 :', next(t1))
print('ex5-4 :', next(t1))
print('ex5-5 :', next(t1))

t2 = gen1()

print('ex5-7 :', list(t2))

print()
print()

def gen2():
    yield from 'AB'
    yield from range(1,4)

t3 = gen2()

print('ex6-1 :', next(t3))
print('ex6-2 :', next(t3))
print('ex6-3 :', next(t3))
print('ex6-4 :', next(t3))
print('ex6-5 :', next(t3))


t4 = gen2()

print('ex6-7 :', list(t4))

print()
print()


def gen3_sub():
    print('sub coroutine')
    x = yield 10
    print('Recv : ', str(x))
    x = yield 100
    print('Recv : ', str(x))

def gen4_main():
    yield from gen3_sub()

t5 = gen4_main()

print('ex7-1 :', next(t5))
print('ex7-1 :', t5.send(7))
print('ex7-1 :', t5.send(77))























































