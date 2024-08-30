import streamlit as st
def sui():
    st.write("수이는 파이썬언어가 어렵지만 열심히 하고 있습니다.")

    st.write("★○★--------------------------------- ★○★")
    st.write("우: 우리들은 어쩌면 만날 운명이었는지 모릅니다.")
    st.write("수: 수많은 연들이 모여서 만나진거겠죠~")
    st.write("민: 민낯으로 인사드립니다. 수이의 첫 웹입니다. 만나서 반가워요")    
    st.image("초록머리앤.jpg")    
    mean  =  st.radio("우수민", ["1:우","2:수", "3:민"],index=None)
    st.write("mean")
    if mean=="1:우":
        st.image("봄꽃먹기.jpg",width=150)
    elif mean=="2:수":
        st.image("갈치한상차림.jpg",width=150)
    elif mean=="3:민":
        st.image("맛있게 웃어요.jpg",width=150)
        st.write("사랑만큼 맛있게 먹어요")