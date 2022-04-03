# Chapter03_01
# 파이썬 심화
# 시퀀스 형

# 컨테이너(Container) : 서로 다른 자료형[list, tuple, collections.deque]
# Flat : 한 개의 자료형 [str, bytes, bytearray, array.array, memoryview]
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists
chars = '!@#$%^&*()_+'
code1 = []

for s in chars:
    code1.append(ord(s))

# Comprehending Lists
code2 = [ord(s) for s in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세
code3 = [ord(s) for s in chars if ord(s) > 40]
code4 = list(filter(lambda x : x > 40, map(ord, chars)))

print('ex1-1 -', code1)
print('ex1-2 -', code2)
print('ex1-3 -', code3)
print('ex1-4 -', code4)
