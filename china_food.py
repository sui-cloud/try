import pandas as pd 

def preprocessing_file(): #꼭  함수로 구조화 시켜 만들기 
    #데이터 불러오기
    df = pd.read_csv("data/101_DT.csv",encoding='euc-kr')

    #필요없는 열 삭제
    df_r = df.drop(['시도별', '항목', '단위', '2024.02 월', '2024.03 월', '2024.04 월',
        '2024.05 월', '2024.06 월', '2024.07 월','Unnamed: 59'],axis=1)

    #해당하는 품목검색(양파, 밀가루, 돼지고기, 자장면)
    df_data = df_r[(df_r['품목별']=='양파')|(df_r['품목별']=='밀가루')|(df_r['품목별']=='돼지고기')|(df_r['품목별']=='자장면')]

    #행열전환 및 인덱스 해제 재조정
    df_data = df_data.set_index("품목별").T.reset_index()

    #열 이름 변경
    df_data = df_data.rename(columns={'index':'년도'})

    print(df_data)

    #전처리 파일 저장
    df_data.to_csv("chianfood.csv")



if __name__=='__main__': #if 한칸 뛰고 씁니다. 나일때만 호출될께요.
    preprocessing_file()    #인수갑니다. 