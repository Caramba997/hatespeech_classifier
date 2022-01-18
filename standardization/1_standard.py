import pandas as pd
import standard as s

df = pd.read_csv('./datasets/1_labeled_data.csv')
st = s.Standardizer()
for idx, item in df.iterrows():
    is_hatespeech = 0
    if item['class'] != 2:
        is_hatespeech = 1
    st.add(is_hatespeech, item['tweet'])

st.export('1')
