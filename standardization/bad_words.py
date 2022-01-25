import pandas as pd
import re

kw_vocab = set()

df_kw = pd.read_csv("datasets/4_harassment-corpus.csv")
for idx, item in df_kw.iterrows():
  if pd.notnull(item["Sexual"]):
    kw_vocab.add(item["Sexual"])
  if pd.notnull(item["Racial"]):
    kw_vocab.add(item["Racial"])
  if pd.notnull(item["Appearance"]):
    kw_vocab.add(item["Appearance"])
  if pd.notnull(item["Intelligence"]):
    kw_vocab.add(item["Intelligence"])
  if pd.notnull(item["Politics"]):
    kw_vocab.add(item["Politics"])
  if pd.notnull(item["Generic"]):
    kw_vocab.add(item["Generic"])
print(len(kw_vocab))

df_vocab = set()
df_kw = pd.read_csv("datasets/7_bad-words.csv")
for idx, item in df_kw.iterrows():
  kw_vocab.add(item[0])
  df_vocab.add(item[0])
print(len(df_vocab), len(kw_vocab))

df_vocab = set()
df_kw = pd.read_csv("datasets/8_Terms-to-Block.csv")
for idx, item in df_kw.iterrows():
  kw_vocab.add(re.sub('"|,', '', item[0]))
  df_vocab.add(re.sub('"|,', '', item[0]))
print(len(df_vocab), len(kw_vocab))


# df = pd.DataFrame(kw_vocab)
# df.to_csv('datasets/bad_words.csv', index=False)