# 한 줄에 하나씩 입력으로 들어와 --> 이거 속도 문제 해결방법이 import sys인건지?

N, M = map(int, input().split())  # map 함수는 결과값은 이터레이터로 반환한다. 고로 list로 변환해주는 작업이 필요하다. 미변환시 주소값이 출력된다.

all_pocketmon = [0] # 리스트 초기화, 0 요소 추가
all_pocketmon_dict = dict() # 딕셔너리 초기화

for i in range(N):
    each_pocketmon = input() # N개 입력(26)
    all_pocketmon.append(each_pocketmon)
    all_pocketmon_dict[each_pocketmon] = i+1 # 키가 each_pocketmon이고 밸류가 i+1이다.
                    # 딕셔너리에 새로운 키값 쌍 추가
                    # 딕셔너리에 요소를 추가할 때는 [key] = value 형식
check_list = [input() for _ in range(M)]

for each in check_list:
    if each.isdigit():  # .isdigit() 문자열이 숫자로만 이루어져 있는지 확인
        print(all_pocketmon[int(each)])  # 숫자인 경우 인트 출력
    else:
        print(all_pocketmon_dict[each])     # 숫자 아닌 경우 each를 키로 가진 포켓몬의 인덱스 출력(인덱스::키)