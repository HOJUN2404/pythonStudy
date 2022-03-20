# section 05
#  반복문

v1 = 1;

for v1 in range(1, 10):
    print('v1 = ', v1);

sum1 = 0
cnt1 = 1

while cnt1 <= 100 :
    sum1 += cnt1
    cnt1 += 1

print('1부터 100의 합 = ', sum1)
print('1부터 100의 합2 = ', sum(range(1, 101)))
print('1부터 100의 짝수 합 = ', sum(range(1, 101, 2))) 


