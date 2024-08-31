import streamlit as st
import random

def gugudan():
    dan = st.number_input("구구단을 입력하세요",value=1)

    if dan>1:
        for i in range(1,10):
        # x=dan*i
            st.write(f"{dan}*{i}={dan*i}")

def recommand_food():
    # 음식추천 프로그램 한식 중식 음식 추천 프로그램 1:중식 2:한식
    c_food=['자장면', '팔보채', '짬뽕', '유산슬', '탕수육']
    k_food=['불고기', '비빔밥', '곰탕', '육개장', '김치찌개' ]

    
    user = st.radio("음식추천", ["중식", "한식"],index=None)
    if user=="중식":
        st.write(f"오늘의 중식 추천 메뉴: {random.choice(c_food)}")
    elif user=="한식":
        st.write(f"오늘의 한식 추천 메뉴: {random.choice(k_food)}")
    else:
        st.write("음식 종류를 선택하세요")


#음식추천 함수 호출해야 실행된다. 
def basic():
    tab1, tab2 = st.tabs(["구구단", "음식추천"])

    with tab1:
        gugudan()
    
    with tab2:
        recommand_food()
basic() 
