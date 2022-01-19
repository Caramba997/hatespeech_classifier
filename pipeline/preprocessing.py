import string
import re
import pandas as pd

def removePunctuation(str):
    return str.translate(str.maketrans('', '', string.punctuation))

def lower(str):
    return str.lower()

def strip(str):
    return re.sub('\s\s+', ' ', str.strip())

def processString(str):
    str = removePunctuation(str)
    str = lower(str)
    str = strip(str)
    return str

def processStandardCsv(fileNumber):
    df = pd.read_csv('./datasets/' + fileNumber + '_standard.csv')
    for idx, item in df.iterrows():
        df.at[idx, 'text'] = processString(item['text'])
    df.rename(columns={'Unnamed: 0': 'index'}, inplace=True)
    df.to_csv('datasets/' + fileNumber + '_preprocessed.csv', index=False)

processStandardCsv('6')