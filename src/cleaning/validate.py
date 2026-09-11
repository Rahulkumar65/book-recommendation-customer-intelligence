import pandas as pd
def validate_books(df):
    checks=[("total_records",len(df),len(df)>0),
            ("duplicate_book_ids",int(df.book_id.duplicated().sum()),df.book_id.duplicated().sum()==0)]
    for c in ["title","author"]:
        m=int(df[c].isna().sum()+(df[c].astype(str).str.strip()=="").sum())
        checks.append((f"missing_{c}",m,m==0))
    for c,lo in [("rating",0),("price",0),("review_count",0)]:
        if c in df:
            x=pd.to_numeric(df[c],errors="coerce")
            bad=int(((x<lo) if c!="rating" else ((x<0)|(x>5))).sum())
            checks.append((f"invalid_{c}",bad,bad==0))
    return pd.DataFrame(checks,columns=["check","value","passed"])
def clean_books(df):
    x=df.copy()
    x["book_id"]=x.book_id.astype(str).str.strip()
    x["title"]=x.title.fillna("").astype(str).str.strip()
    x["author"]=x.author.fillna("Unknown").astype(str).str.strip()
    for c in ["rating","price","review_count"]:
        if c in x: x[c]=pd.to_numeric(x[c],errors="coerce")
    return x.drop_duplicates("book_id").query("title != ''").copy()
