# Chapter03_02
# 파이썬 심화
# 시퀀스형
# 해시테이블( Hashtable ) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# Dict 구조
print('ex1-1 :')
# print(__builtins__.__dict__)

print()
print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print('ex1-2 :', hash(t1))
# print('ex1-3 :', hash(t2))

# 지능형 딕셔너리
import csv

# 외부 CSV TO List of tuple

with open('./resource/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print('ex2-1',)
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()

print('ex2-2',)
print(n_code1)

print()
print()

print('ex2-3',)
print(n_code2)

# Dict Setdefault 예제
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5')
)


new_dict1 = {}


# No use setdefault


# Use setdefault