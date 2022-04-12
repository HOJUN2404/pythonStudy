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


from collections import abc

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

























