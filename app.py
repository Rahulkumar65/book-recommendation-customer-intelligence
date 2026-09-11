from pathlib import Path
import pandas as pd,streamlit as st
from dotenv import load_dotenv
from src.analytics.rfm import build_rfm,segment_rfm
from src.recommendation.collaborative import ItemCollaborativeRecommender
from src.recommendation.content import ContentRecommender
from src.nlp.sentiment import analyze_reviews
from src.llm.business_analyst import ask_llm
load_dotenv(); st.set_page_config(page_title="Book Intelligence",page_icon="📚",layout="wide")
B=pd.read_csv("data/processed/books_clean.csv"); U=pd.read_csv("data/processed/users.csv"); R=pd.read_csv("data/processed/ratings.csv"); P=pd.read_csv("data/processed/purchases.csv"); V=pd.read_csv("data/processed/reviews.csv")
st.title("📚 Book Recommendation & Customer Intelligence")
a,b,c,d,e=st.tabs(["Executive","Customers","Recommendations","Reviews","AI Analyst"])
with a:
    rev=(P.quantity*P.price).sum(); x,y,z,q=st.columns(4); x.metric("Customers",len(U)); y.metric("Books",len(B)); z.metric("Purchases",len(P)); q.metric("Revenue",f"₹{rev:,.0f}")
    g=P.merge(B[["book_id","genre"]],on="book_id"); g["revenue"]=g.quantity*g.price; st.bar_chart(g.groupby("genre").revenue.sum().sort_values())
with b:
    r=segment_rfm(build_rfm(P)); st.dataframe(r,use_container_width=True); st.bar_chart(r.segment.value_counts())
with c:
    uid=st.selectbox("Customer",U.user_id.tolist()); cm=ContentRecommender().fit(B); cf=ItemCollaborativeRecommender().fit(R); rec=cf.recommend(uid,10)
    st.dataframe(B[B.book_id.isin(rec)][["book_id","title","author","genre","rating"]],use_container_width=True)
with d:
    s=analyze_reviews(V); st.bar_chart(s.sentiment.value_counts()); st.dataframe(s,use_container_width=True)
with e:
    question=st.text_input("Ask a business question"); 
    if st.button("Analyze"):
        g=P.merge(B[["book_id","genre"]],on="book_id"); g["revenue"]=g.quantity*g.price
        context=f"Customers: {len(U)}\nBooks: {len(B)}\nRevenue: {g.revenue.sum():.2f}\nRevenue by genre:\n{g.groupby('genre').revenue.sum().to_string()}"
        try: st.write(ask_llm(question,context))
        except Exception as ex: st.error(str(ex))
