# section 05-2

names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

# for v in names :
#     print("You are ", v)

my_info = {
    "name" : "Kim",
    "age" : 25,
    "city" : "Incheon"
}

# 기본값은 키
for key in my_info :
    print("my_info", key)

# 값 
for key in my_info.values():
    print("my_info", key)

# 키
for key in my_info.keys():
    print("my_info", key)

#  키 and 값
for k1, v1 in my_info.items():
    print("my_info", k1, v1)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())    



# Break 문
# Continue

numbers = [14, 3, 7, 20, 32, 15, 22, 55, 102]

for num1 in numbers :
    if num1 == 33:
        print("Found : 33 !!")
        break
    else:
        print("Not Found")
else:
    print("Not Found 33......")

