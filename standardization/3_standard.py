import pandas as pd
import standard as s

df = pd.read_csv('./datasets/3_en_dataset_with_stop_words.csv')
st = s.Standardizer()
for idx, item in df.iterrows():
    st.add(1, item['tweet'], item['target'])

st.export('3')
