# Chapter 04_2
# 파이썬 심화
# 일급 함수 (일급 객체)
# Decorator & Closer 

# 파이썬 변수 범위(Global)



def func_v1(a):
    print(a)
    print(b)

b = 10

# 예외
# func_v1(5)

def func_v2(a):
    print(a)
    print(b)
    b=5

# func_v2(5)


# 예제 3
b = 10

def func_v3(a):
    print(a)
    print(b)
    b = 5

#  func_v3(5)

from dis import dis

print('ex1-1 -')
print(dis(func_v3))

print()
print()



# Closure ( 클로저 )
# 반환되는 내부 함수에 대해서 선언된 연결을 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다.

a = 10

print('ex2-1 -', a+10)
print('ex2-2 -', a+100)

# 결과를 누적할 수 없을까?
print('ex2-3 -', sum(range(1,51)))
print('ex2-4 -', sum(range(51,101)))

print()
print()


# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []
    
    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
avg_cls = Averager()

# 누적 확인
print('ex3-1 -', avg_cls(10))
print('ex3-2 -', avg_cls(35))
print('ex3-3 -', avg_cls(40))

print()
print()


# 클로저( Closure )

def closure_avg1():

    # Free Variable (자유영역.... 클로저 영역이라고 한다...?)
    series = []

    def averager(v):
        series.append(v)
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_avg1()

print('ex4-1 -', avg_closure1(15))
print('ex4-2 -', avg_closure1(35))
print('ex4-3 -', avg_closure1(40))


print()
print()

print('ex5-1 -', dir(avg_closure1))
print()
print('ex5-2 -', dir(avg_closure1.__code__))
print()
print('ex5-3 -', avg_closure1.__code__.co_freevars)

print()
print()
print()
print()


def closure_avg2():
    # Free Variable
    cnt = 0
    total = 0

    # Closure Section
    def averager(v):
        # nonlocal이 없으면 잘못된 Closure 사용 예이다.
        nonlocal cnt, total
        cnt += 1
        total += v
        print('def2 >>> {} / {}'.format(total, cnt))
        return total / cnt
    return averager

avg_closure2 = closure_avg2()

print('ex5-5 :', avg_closure2(15))
print('ex5-6 :', avg_closure2(35))
print('ex5-7 :', avg_closure2(40))


# Decorator 
# 1. 중복제거, 코드간결
# 2. 클로저보다 문법 간결
# 3. 조합해서 사용하기 용이하다.


import time

def perf_clock(func):
    def perf_clocked(*args):
        # 시작시간
        st = time.perf_counter()
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 출력
        print('Result : [%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked        


@perf_clock
def time_func(second):
    time.sleep(second)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

@perf_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)

print()
print()
print()

# Decorator 미사용

# non_deco1 = perf_clock(time_func)
# non_deco2 = perf_clock(sum_func)
# non_deco3 = perf_clock(fact_func)

# print('ex7-1 :', non_deco1, non_deco1.__code__.co_freevars)
# print('ex7-1 :', non_deco2, non_deco2.__code__.co_freevars)
# print('ex7-1 :', non_deco3, non_deco3.__code__.co_freevars)

# print()
# print()

# print('*'*20, 'Called Non Decorator -> time_func')
# print('ex7-4 :')
# non_deco1(0)
# print('*'*20, 'Called Non Decorator -> sum_func')
# print('ex7-5 :')
# non_deco2(100, 200, 300, 400, 100000)
# print('*'*20, 'Called Non Decorator -> fact_func')
# print('ex7-6 :')
# non_deco3(100)

print()
print()
print()

print('*'*20, 'Called Decorator -> time_func')
print('ex7-7 :')
time_func(0)

print('*'*20, 'Called Decorator -> sum_func')
print('ex7-8 :')
sum_func(10, 20, 30, 40, 50)

print('*'*20, 'Called Decorator -> fact_func')
print('ex7-9 :')
fact_func(10)












