# Chapter06-1
# 흐름제어, 병행처리(Concurrency)
# 제네리엍, 반복형
# Generator

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args
# 반복형 객체 내부적으로 iter 함수 사용, 제네레이터 동작원리, yeild from

# 반복가능한 이유는 -> iter(x) 함수 호출하기 때문


t = 'ABCDEF'

# for 사용
for c in t:
    print('ex1-1 :', c)

print()

# while 사용

w = iter(t)

while True:
    try:
        print('ex1-2 :', next(w))
    except StopIteration as log:
        print(log)
        break


from ast import Yield
from collections import abc
from email import generator

# 반복형 확인
print('ex1-3 :', hasattr(t, '__iter__'))
print('ex1-4 :', isinstance(t, abc.Iterable))

print()
print()
print()


# next 사용

class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration()
        self._idx += 1
        return word

    def __iter__(self):
        print('Called __iter__')
        return self

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitIter('Who is the fucking guy')

print('ex2-1 :', wi)
print('ex2-2 :', next(wi))
print('ex2-3 :', next(wi))
print('ex2-3 :', next(wi))
print('ex2-3 :', next(wi))
print('ex2-3 :', next(wi))
# print('ex2-3 :', next(wi))


print()
print()
print()



# Generator 패턴
# 1. 지능형리스트, 딕셔너리, 집합 -> 데이터 셋이 증가될 경우 메모리 사용량 증가 -> 제너레이터 완화
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3. 딕셔너리, 리스트 한 번 호출할 때마다 하나의 값만 리턴 -> 아주 작은 메모리 양을 필요로 함

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitIter('Who is the fucking guy')

wt = iter(wg)

print('ex3-1 :', wt)
print('ex3-2 :', next(wt))
print('ex3-3 :', next(wt))
print('ex3-4 :', next(wt))
print('ex3-5 :', next(wt))
print('ex3-6 :', next(wt))
# print('ex2-3 :', next(wt))


print()
print()
print()

# Generator 예제 1

def generator_ex1():
    print('start!')
    yield 'AAA'
    print('continue')
    yield 'BBB'
    print('end')

temp = iter(generator_ex1())

print('ex4-1 :', next(temp))
print('ex4-2 :', next(temp))
# print('ex4-3 :', next(temp))

for v in generator_ex1():
    pass
    # print('ex4-3 :', v)


# Generator 예제 2

temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print('ex5-1 :', temp2)
print('ex5-2 :', temp3)

for i in temp2:
    print('ex5-3 :', i)

for i in temp3:
    print('ex5-4 :', i)

print()
print()
print()

# Generator 예제3 (자주 사용하는 함수..)

import itertools

gen1 = itertools.count(1, 2.5)

print('ex6-1 :', next(gen1))
print('ex6-2 :', next(gen1))
print('ex6-3 :', next(gen1))
print('ex6-4 :', next(gen1))
# . . . 무한


# 조건
print()
print()

gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print('ex 6-5 :', v)


# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print('ex6-6 :', v)

print()
print()

# 누적합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print('ex6-7 :', v) 


print()
print()

# 연결
gen5 = itertools.chain('ABCDE', range(1, 11, 2))

print('ex6-8 :', list(gen5))


# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))

print('ex6-9 :', list(gen6))

# 개별
gen7 = itertools.product('ABCDE')
print('ex6-10 :', list(gen7))

# 연산
gen8 = itertools.product('ABCDE', repeat=2)
print('ex6-11 :', list(gen8))

# 그룹화
gen9 = itertools.groupby('AAABBCCCCCDDEEEEE')
# print('ex6-12 :', list(gen9))

for chr, group in gen9:
    print('ex6-12 :', chr, ' : ', list(group))
































