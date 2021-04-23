print("1. 입력한 수식 계산 2. 두수 사이의 합계:")
ans = input()
if ans == '1' :
    print("***수식을 입력하세요:")
    a=input()
    print("{0}의 결과는 {1} 입니다." .format(a, eval(a)))
elif ans == '2' :
    b = int(input("첫 번째 숫자를 입력하세요 : " ))
    c = int(input("두번째 숫자를 입력하세요 : " ))
    result = 0
    for i in range(b, c+1):
        result = result + i
    print("{0} + ... +{1}는 {2} 입니다" .format(b,c,result))
else :
        print("end")
        
        
# .format 으로 한점 : b, c 는 int 형이지만 result 의 형은 string 이다.
# 서로 형이 다르면 %(b, c, result) 계산시 오류가 난다.
# 그래서 .format()으로 맞춰줘야함. 