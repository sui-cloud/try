# Main
import k_food as kf
import fast_food as ff
import bunsik as bs

while True:
    print("추천 맛집 종류예요: ")
    print("*"*30)
    print("1. 한식")
    print("2. 패스트푸드")
    print("3. 분식")
    print("*"*30)

    menu_number = input("번호를 입력하세요: ")

    if menu_number == '1':
        print("\"한식\"을 선택하셨네요!")
        if not kf.k_food():             # 예산에 맞는 메뉴가 없을 경우 앞 모듈의 False값을 받아
            print("다시 선택해 주세요")
        else:
            break                       # 예산에 맞는 메뉴를 찾았으므로 반복문 중지
    elif menu_number == '2':
        print("\"패스트푸드\"를 선택하셨네요!")
        if not ff.fast_food():
            print("다시 선택해 주세요")
        else:
            break
    elif menu_number == '3':
        print("\"분식\"을 선택하셨네요!")
        if not bs.bunsik():
            print("다시 선택해 주세요")
        else:
            break
    else:
        print("잘못 입력하셨어요! 다시 선택해 주세요")