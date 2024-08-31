# Main
import streamlit as st
import k_food as kf
import fast_food as ff
import bunsik as bs

def main_food():

    menu_number = st.radio("메뉴선택", ["1:한식","2:패스트푸드", "3:분식"],index=None)
    st.write("추천 맛집 종류예요: ")
    st.image("공복음식.jpg",width=500)
    # st.write("1. 한식")
    # st.write("2. 패스트푸드")
    # st.write("3. 분식")
    
    
    # menu_number = st.number_input("번호를 입력하세요: ",value=1)
    
    if menu_number == '1:한식':
        st.write("\"한식\"을 선택하셨네요!")
        # kf.k_food()
        if not kf.k_food():             # 예산에 맞는 메뉴가 없을 경우 앞 모듈의 False값을 받아
            st.write("다시 선택해 주세요")
        # else:
            
                                  # 예산에 맞는 메뉴를 찾았으므로 반복문 중지
    elif menu_number == '2:패스트푸드':
        st.write("\"패스트푸드\"를 선택하셨네요!")
        # ff.fast_food()
        if not ff.fast_food():
            st.write("다시 선택해 주세요")
        # else:
        #     break
    elif menu_number == '3:분식':
        st.write("\"분식\"을 선택하셨네요!")
        # bs.bunsik()
        if not bs.bunsik():
            st.write("다시 선택해 주세요")
main_food()           
    
        # else:
            # break
    # else:
        # st.write("잘못 입력하셨어요! 다시 선택해 주세요")
