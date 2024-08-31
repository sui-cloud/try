import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


#데이터 불러오기
df = pd.read_csv("penguins_size.csv")
#데이터 전처리하기
#결측치 처리하기-삭제 
df.dropna(inplace=True)
df.isnull().sum()
#펭귄 성별 고유값 구하기
df['sex'].unique()
#펭귄 성별 중 잘못된 값 삭제하기
df[df['sex']=='.']
df.drop(axis=0, inplace=True, index=336)
#펭귄 종별 개수 구하기
df['species'].value_counts()
sns.countplot(x='species', data=df)
plt.show()
#펭귄 종별 날개 길이를 박스 플롯으로 시각화하기
plt.figure(figsize=(8,6))
sns.boxplot(x='species', y='flipper_length_mm', hue='species', data=df)
plt.show()
#특징값을 산점도로 시각화하기
sns.scatterplot(x='culmen_depth_mm', y='culmen_length_mm', hue='species', data=df)
plt.show()
sns. scatterplot(x='flipper_length_mm', y='culmen_length_mm', hue='species', data=df)
plt.show()
#특징과 타깃 선정하기
df1 = df[['culmen_depth_mm', 'culmen_length_mm', 'flipper_length_mm', 'species']]
dataset = df1.values
X = dataset[:,:-1]
y = dataset[:,-1]
print('특징모양:', X.shape)
print('타깃모양:', y.shape)
#데이터 정규화하기
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_scaled[0]

#훈련데이터, 테스트 데이터 분할하기
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3,stratify=y, random_state=0)

print("훈련 데이터:", X_train.shape, y_train.shape)
print("테스트 데이터:", X_test.shape, y_test.shape)
#모델 생성하기-최근접 이웃 알고리즘으로 학습하기
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
print("훈련 데이터를 이용한 모델 분류 정확도:", knn.score(X_train, y_train))
#모델 평가 및 예측하기
#모델 평가하기
print("테스트 데이터를 이용한 모델 성능 평가:", knn.score(X_test, y_test))
#최적의 K구하기
for k in range(2,11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    score = knn.score(X_test, y_test)
    print('k: %d, accuracy: %2f' %(k, score*100))
    #테스트 데이터 예측하기
predictions =  knn.predict(X_test)
print(predictions[:5])
print(y_test[:5])


plt.figure(figsize=(8,6))

conf = confusion_matrix(y_test, predictions)
sns.heatmap(conf, annot=True, cmap= 'BuPu')

plt.title("Penguin Classification")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
#모델 활용하기
#새로운 데이터프레임 생성하기
# from google.colab import files
# uploded = files.upload()

df_new = pd.read_csv("penguin_new.csv")
df_new.head()

#데이터 정규화하기
dataset_new = df_new.values
new_scaled = scaler.fit_transform(dataset_new)

print(knn.predict(new_scaled))
