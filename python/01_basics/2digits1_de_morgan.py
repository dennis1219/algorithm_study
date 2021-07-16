print('2자리의 양수를 입력하세요.')

while True:
    no = int(input('값을 입력하세요.: '))
    if not(no < 10 or no > 99):
        break

print(f'입력받은 양수는 {no}입니다.')

#De Morgan's law.