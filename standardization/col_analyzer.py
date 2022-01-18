import pandas as pd
import standard as s

df = pd.read_csv('./datasets/5_train.csv')

types = set(df['target'].to_list())
print(types)
# processed = set()

# for item in types:
#     subs = item.replace(' ','').split('_')
#     for sub in subs:
#         processed.add(sub)

# print(processed)
