import re
import pandas as pd
POS={"excellent","amazing","great","love","loved","wonderful","fantastic","enjoyed","interesting","beautiful","helpful","best"}
NEG={"boring","bad","poor","hate","hated","awful","weak","slow","confusing","disappointing","worst"}
def one(t):
    w=re.findall(r"[a-z']+",str(t).lower()); s=sum(x in POS for x in w)-sum(x in NEG for x in w)
    return pd.Series(["positive" if s>0 else "negative" if s<0 else "neutral",s])
def analyze_reviews(df):
    x=df.copy(); x[["sentiment","sentiment_score"]]=x.review_text.apply(one); return x
