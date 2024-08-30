# 스트림릿은 웹에서 실행된다. 
import streamlit as st
import electronic0806 as ec
import pybasic as pb #파이썬기초
import project as pr #각자 프로젝트
import car_predict as cp
import penguinap as pe
import sui as su



#로그인 화면
st.sidebar.title("로그인")
user_id = st.sidebar.text_input("아이디(ID) 입력", value='abc', max_chars=10)
user_pw = st.sidebar.text_input("패스워드 입력", value='',type="password")

if user_pw=="1234" and user_id=="abc":
    st.sidebar.title("★수이의 포트폴리오★")
    #st.image("빨간머리앤셜리.jpg")

    menu  =  st.sidebar.radio("메뉴선택", ["파이썬기초","탐색적 분석: 전기자동차", "머신러닝","팀별프로젝트","수이는","펭귄"],index=None)
    st.sidebar.write(menu)

    if menu=="탐색적 분석: 전기자동차":
        ec.elec_exe()
    elif menu=="머신러닝":
        cp.aiml_main()
        # st.header("공사중")    
    elif menu=="파이썬기초":
        pb.basic()
    elif menu=="팀별프로젝트":
        pr.main_food()
    elif menu=="수이는": #파일로 만들어서 호출하기
        #st.write("수이는 파이썬언어가 어렵지만 열심히 하고 있습니다.")  
        #st.image("초록머리앤.jpg") 
        su.sui()
    elif menu=="펭귄":
        pe.penguin()


