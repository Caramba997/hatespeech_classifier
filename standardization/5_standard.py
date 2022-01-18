import pandas as pd
import standard as s

df = pd.read_csv('./datasets/5_train.csv')
st = s.Standardizer()
for idx, item in df.iterrows():
    is_hatespeech = 0
    if item["toxic"] == 1 or item["severe_toxic"] == 1:
        is_hatespeech = 1
        st.add(1, item['comment_text'], 'toxic')
    if item["obscene"] == 1:
        is_hatespeech = 1
        st.add(1, item['comment_text'], 'obscene')
    if item["threat"] == 1 or item["insult"] == 1:
        is_hatespeech = 1
        st.add(1, item['comment_text'], 'other')
    if item["identity_hate"] == 1:
        is_hatespeech = 1
        st.add(1, item['comment_text'], 'origin')
    if is_hatespeech == 0:
        st.add(1, item['comment_text'], 'other')
        
st.export('5')
