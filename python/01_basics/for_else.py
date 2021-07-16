import random

n = int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end = ' ')
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break

else:
    print('\n난수 생성을 종료합니다.')


#for문과 같은 레벨에 else를 둬서 break 없이 빠져나온 경우를 처리한다.