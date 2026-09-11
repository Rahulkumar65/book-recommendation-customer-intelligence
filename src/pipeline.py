import pandas as pd
from src.analytics.rfm import build_rfm,segment_rfm
from src.recommendation.collaborative import ItemCollaborativeRecommender
from src.recommendation.evaluation import precision_at_k,recall_at_k,ndcg_at_k
from src.nlp.sentiment import analyze_reviews
def run():
    B=pd.read_csv("data/processed/books_clean.csv"); U=pd.read_csv("data/processed/users.csv"); R=pd.read_csv("data/processed/ratings.csv"); P=pd.read_csv("data/processed/purchases.csv"); V=pd.read_csv("data/processed/reviews.csv")
    segment_rfm(build_rfm(P)).to_csv("data/processed/rfm_segments.csv",index=False)
    rows=[]
    for uid,g in R.groupby("user_id"):
        g=g.sort_values("timestamp")
        if len(g)<3:continue
        train=g.iloc[:-1]; test=set(g.tail(1).book_id)
        rec=ItemCollaborativeRecommender().fit(train).recommend(uid,5)
        rows.append({"user_id":uid,"precision_at_5":precision_at_k(rec,test),"recall_at_5":recall_at_k(rec,test),"ndcg_at_5":ndcg_at_k(rec,test)})
    m=pd.DataFrame(rows); pd.DataFrame([{"model":"collaborative","precision_at_5":m.precision_at_5.mean(),"recall_at_5":m.recall_at_5.mean(),"ndcg_at_5":m.ndcg_at_5.mean(),"evaluated_users":len(m)}]).to_csv("data/processed/model_metrics.csv",index=False)
    analyze_reviews(V).to_csv("data/processed/review_sentiment.csv",index=False)
    print("Pipeline complete.")
if __name__=="__main__":run()
