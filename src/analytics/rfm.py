import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
def build_rfm(p):
    x=p.copy(); x.purchase_date=pd.to_datetime(x.purchase_date); x["revenue"]=x.quantity*x.price
    snap=x.purchase_date.max()+pd.Timedelta(days=1)
    r=x.groupby("user_id").agg(last_purchase=("purchase_date","max"),frequency=("purchase_id","nunique"),monetary=("revenue","sum")).reset_index()
    r["recency"]=(snap-r.last_purchase).dt.days
    return r[["user_id","recency","frequency","monetary"]]
def segment_rfm(rfm,k=4):
    x=rfm.copy(); Z=StandardScaler().fit_transform(x[["recency","frequency","monetary"]])
    x["cluster"]=KMeans(n_clusters=k,random_state=42,n_init=20).fit_predict(Z)
    s=x.groupby("cluster")[["recency","frequency","monetary"]].mean()
    score=s.frequency.rank(pct=True)+s.monetary.rank(pct=True)-s.recency.rank(pct=True)
    order=score.sort_values(ascending=False).index
    names=["High Value Readers","Frequent Readers","Occasional Readers","At Risk / Inactive"]
    mp={c:names[min(i,3)] for i,c in enumerate(order)}
    x["segment"]=x.cluster.map(mp); return x
