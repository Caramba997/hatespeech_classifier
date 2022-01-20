import string
import re
import pandas as pd
import nltk

stopwords = nltk.corpus.stopwords.words('english')

def removePunctuation(str):
    return str.translate(str.maketrans('', '', string.punctuation))

def lower(str):
    return str.lower()

def strip(str):
    return re.sub('\s\s+', ' ', str.strip())

def removeMentions(str):
    return re.sub('@\S+', '', str)

def removeEncodedSymbols(str):
    return re.sub('&#\d+', '', str)

def removeLinks(str):
    return re.sub('http:\/\/\S+|https:\/\/\S+', '', str)

def removeStopWords(str):
    words = str.split(' ')
    no_stopwords = [e for e in words if e not in stopwords]
    return ' '.join(no_stopwords)

def processString(str):
    str = removeMentions(str)
    str = removeEncodedSymbols(str)
    str = removeLinks(str)
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

def csvRemoveStopwords(fileNumber):
    df = pd.read_csv('./datasets/' + fileNumber + '_standard.csv')
    for idx, item in df.iterrows():
        df.at[idx, 'text'] = processString(removeStopWords(item['text']))
    df.to_csv('datasets/' + fileNumber + '_no_stopwords.csv', index=False)

# processStandardCsv('5')
csvRemoveStopwords('5')