import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

#한글 글꼴
plt.rc('font',family='malgun gothic')

def basic():
    #파일 불러우기
    df=pd.read_csv('한국전력공사_지역별 전기차 현황정보_20230331.csv', encoding='euc_kr')

    #피벗 해제(열의 데이터로 변환)
    df_melt=pd.melt(df,id_vars='기준일', value_vars=['서울', '인천', '경기', '강원', '충북', '충남', '대전', '세종', '경북', '대구', '전북',
        '전남', '광주', '경남', '부산', '울산', '제주', '합계'],var_name='지역', value_name='자동차수')
    #'년', '월' 파생변수 생성
    df_melt['년']=df_melt['기준일'].str[:4]
    df_melt['월']=df_melt['기준일'].str[5:7]

    return df_melt

def region_mean(df_melt):
    ########################################################
    #지역별, 년도별 자동차수 평균 계산 -pivot_table
    year_region_da =  round(pd.pivot_table(df_melt,index='년',columns='지역',values='자동차수',aggfunc='mean'),1)
    st.dataframe(year_region_da)
    year_region_da = year_region_da.T
    #데이터 프레임 이용한 차트
    # year_region_da.plot(kind='bar',rot=0)
    #행의 데이터 추출, df[(조건1)]|[(조건2)], df[(조건1)]&[(조건2)] 오렌지3 셀렉트로울즈 
    region_query = year_region_da[year_region_da.index!='합계'] #query는 조건을 넣는다.라는 뜻
    #판다스의 데이터프레임 이용한 차트 작성
    #df.plot(kind='bar',x='필드', y='필드)
    # 행의 데이터 추출, df[(조건1)]|[(조건2)], df[(조건1)]&[(조건2)] 오렌지3 셀렉트로울즈 
    #df_melt[df_melt['년']=='2023']
    #region_query = year_region_da[year_region_da.index!='합계']
    #데이터 프레임 이용한 차트
    # year_region_da.plot(kind='bar',rot=0)
    ax = region_query.plot(kind='bar', rot=0)
    fig = ax.get_figure()
    st.pyplot(fig)

def mean_2023(df_melt): 
    #######################################################################
    #2023년 분기별 분석
    df_melt_2023=df_melt[df_melt["년"]=='2023']
    df_melt_2023=df_melt_2023[df_melt_2023['지역'] !="합계"]

    df_2023=pd.pivot_table(df_melt_2023, index='지역', columns='월', values='자동차수', aggfunc='mean')
    st.dataframe(df_2023.T) #데이타프레임=테이블은 인터렉션 안 일어난다.
    #df_2023 = df_2023.T 

    ax = df_2023.plot(kind='bar',rot=0)# 차트
    fig = ax.get_figure()# 도화지
    st.pyplot(fig)
     #plt.show()

def quarter_mean(df_melt):    
    #####################################################################
    #2022년 분기별 분석
    df_2022 = df_melt[df_melt['년']=='2022']
    df_2022 = df_2022[df_2022['지역'] !="합계"]
    #데이터 타입을 '정수'로 변환
    df_2022['월']=df_2022['월'].astype(int)

    df_2022['분기']=np.where((df_2022['월']>=1)&(df_2022['월']<=3),"1분기", np.where((df_2022['월']>=4)&(df_2022['월']<=6), "2분기", np.where((df_2022['월']>=7)&(df_2022['월']<=9), "3분기", "4분기"))) # np.where(조건문, 참값, 거짓값)
    #통계1: pivot_table
    df_2022_da = round(pd.pivot_table(df_2022,index='지역',columns='분기',values='자동차수', aggfunc='mean'),0)
    st.dataframe(df_2022_da.T)
    # #통계2:group_by
    # df_2022_da2 = df_2022.groupby(['지역','분기'])[['자동차수']].mean().reset_index()
    # print(df_2022_da2)
    # 판다스를 이용한 차트 작성
    #df.plot()
    ax = df_2022_da.plot(kind='bar',rot=0)
    fig = ax.get_figure()
    st.pyplot(fig)
    #plt.show()

#main 실행
#이름은 다르고 내용은 같다. 받고 주고 
def elec_exe():
    menu = st.selectbox("분석내용",["선택","지역별/연도별분석", "2023_지역별분석","2022_분기별분석"])
    # st.header("탐색적 분석 : 전기자동차 데이터 분석")
    df_melt = basic()
    if menu=="지역별/연도별분석":
        region_mean(df_melt)
    elif menu=="2023_지역별분석":
        mean_2023(df_melt) #2023년 지역별 분석
    elif menu=="2022_분기별분석":
        quarter_mean(df_melt) # 2022년 분기별 분석
    else:
        st.image("빨간머리앤셜리.jpg",width=500) 


# while True:
#     menu = int(input("메뉴 입력(1:지역별/년도별 분석, 2:2023분석, 3:2022년 분기별 분석 0:종료)"))
#     if menu==1:
#         region_mean(df_melt)
#     elif menu==2:
#         mean_2023(df_melt)
#     elif menu==3:
#         quarter_mean(df_melt)
#     elif menu==0:
#         break    
#     else:
#         print("입력 오류")

if __name__=='__main__': #내가 나를 부를때 함수호출시만 실행 남이 부를때는 실행 안함
    elec_exe()


