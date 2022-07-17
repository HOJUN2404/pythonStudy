# # Section02-1
# # Print 구문이해 

# # 기본출력 

# print('Test Hojun');
# print("큰따옴표 테스트 ");
# print("""큰 따옴표 세개??""");
# print('''작은따옴표 세개???''');

# print()

# # Separator 옵션 사용

# print('T', 'E', 'S', 'T', sep='');
# print('2021', '02', '19', sep="-");

# # end 옵션 사용
# print('Welcome To ', end='');
# print('the black parade', end='');
# print()

# # format 사용
# print('{} and {}'.format('You', 'Me'));
# print("{0} and {1} and {0}".format('You', 'Me'));
# print("{a} are {b}".format(a="you", b="Me"));

# # %s는 문자, %d 는 정수 %f 는 실수 이건 이미 알고있다...

# print("Test1: %5d, Price: %4.2f" %(773, 6534.123));
# print("Test1: {0: 5d}, Price: {1:4.2f}".format(776, 6534.123));
# print("Test1: {a: 5d}, Price: {b:4.2f}".format(a=776, b=6534.12322));

# # Escape 코드

# # \t 는 탭키
# # \n 은 띄어쓰기  이것만 알면돼 솔직히 ;; 

# print("'y\no\nu'");
# print("\"you\"");
# print();







# print();
# print("여기부터");

# testVar = 555.2

# print(type(testVar))

# print(id(testVar))

# testVar = 545

# print(id(testVar))


# def 

# def open_account():
#     print("새로운 계좌 생성")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액 {0} 원입니다.".format(balance + money))
#     return balance + money

# balance = 0 #잔액
# balance = deposit(balance, 1000)
# print(balance)




def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance.money): #출금
    if balance >= money:  #출금 가능
     print ("출금이 완료되었습니다. 잔액 {0} 원입니다. ".format(balance - money))
     return balance - moeny
     
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))

def withdraw_night(balance, money): #저녁에 출금
    comission = 100 #수수료 100원
    return comission, balance - money - comission 

balance = 0 #잔액
balance = deposit(balance, 1000)
balance - withdraw(balance, 2000)
comission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다. ".format(comission, balance))