number = int(input())  # 속도 개선을 위해 보통 import sys를 사용하는 듯 하다.

sList = list()
result = list()

for i in range(number):     # def로 객체지향으로 만들지 않아도 괜찮나?
    command = input()       # number 갯수 만큼 명령 입력
    if command == 'size':
        count = 0
        for i in sList:
            if type(i) == type(int()):  # 정수이면 참, 정수가 아니면 거짓.
                count += 1   # 정수타입 요소의 갯수를 저장
        result.append(count)
    elif command == 'pop':
        if not sList:
            result.append(-1)   # 정수가 없는 경우에는 -1을 출력(저장)
        else:
            result.append(sList.pop()) # 가장 위에 있는 정수를 빼고, 그 수를 출력
    elif command == 'empty':
        if sList:
            result.append(0) # 리스트에 0추가
        else:
            result.append(1)  # 리스트에 1 추가
    elif command == 'top':
        if sList:
            result.append(sList[-1]) # 가장 뒤에 있는(위에 있는) 정수 출력
        else:
            result.append(-1)   # 정수 없으면 -1 출력(저장)
    elif command[0:4] == 'push':
        sList.append(int(command.split()[-1]))

for i in result:
    print(i)