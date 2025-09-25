

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import os


# NanumGothic 폰트 경로 지정 및 설정
font_path = os.path.join(os.path.dirname(__file__), '../fonts/NanumGothic-Regular.ttf')
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

st.title("간단한 데이터 시각화 예시")

# 예시 데이터 생성
data = {
	'과일': ['사과', '바나나', '오렌지', '포도', '키위'],
	'수량': [10, 15, 7, 12, 5],
	'가격': [1000, 500, 1200, 2000, 1500]
}
df = pd.DataFrame(data)

st.subheader("데이터 테이블")
st.dataframe(df)


st.subheader("수량 바 차트")
fig1, ax1 = plt.subplots()
sns.barplot(x='과일', y='수량', data=df, ax=ax1)
for label in ax1.get_xticklabels():
	label.set_fontproperties(font_prop)
ax1.set_xlabel('과일', fontproperties=font_prop)
ax1.set_ylabel('수량', fontproperties=font_prop)
st.pyplot(fig1)


st.subheader("가격 파이 차트")
fig2, ax2 = plt.subplots()
ax2.pie(df['가격'], labels=df['과일'], autopct='%1.1f%%', textprops={'fontproperties': font_prop})
ax2.set_title('과일별 가격 비율', fontproperties=font_prop)
st.pyplot(fig2)
