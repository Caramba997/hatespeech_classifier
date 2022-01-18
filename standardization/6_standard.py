import pandas as pd
import standard as s
import tweepy
import tqdm

client = tweepy.Client(
    consumer_key="rW70D1dXs6WSwL1bSlbWyYr8y",
    consumer_secret="DmwXIs1rwdXXYxRTBrogkkzGhDuHbyHHuJgQCIkXl2tu7ihSus",
    access_token="1483376979537707009-E31bDz7rBm6UEjLnhKvrsPSgU5iyHt",
    access_token_secret="kNFjdqEJDv3q1pWUR5WIbfUm092zLIAn77RahueRfipfK"
)
fields = ["id", "text"]

df = pd.read_csv('./datasets/6_NAACL_SRW_2016.csv')
st = s.Standardizer()
types = {}
ids = []
for idx, item in df.iterrows():
    types[item["id"]] = item["type"]
    ids.append(item["id"])
    if len(ids) == 100:
        tweets = client.get_tweets(ids=ids, tweet_fields=fields, user_auth=True).data
        if tweets:
            for tweet in tweets:
                result_type = types[tweet["id"]]
                is_hatespeech = 1
                if result_type == "none":
                    is_hatespeech = 0
                st.add(is_hatespeech, tweet["text"], result_type)
        types = {}
        ids = []

st.export("6")
