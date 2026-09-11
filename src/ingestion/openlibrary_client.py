import argparse, requests, pandas as pd
def fetch(query,limit=50):
    r=requests.get("https://openlibrary.org/search.json",params={"q":query,"limit":limit},timeout=20); r.raise_for_status()
    rows=[]
    for d in r.json().get("docs",[]):
        rows.append({"book_id":(d.get("key") or "").replace("/works/",""),"title":d.get("title"),"author":", ".join(d.get("author_name",[])[:3]),
        "genre":", ".join(d.get("subject",[])[:5]),"publisher":", ".join(d.get("publisher",[])[:3]),"publication_date":d.get("first_publish_year"),
        "language":", ".join(d.get("language",[])[:3]),"description":"","price":None,"rating":None,"review_count":d.get("ratings_count",0)})
    return pd.DataFrame(rows)
if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--query",required=True); p.add_argument("--limit",type=int,default=50); p.add_argument("--output",default="data/raw/api_books.csv"); a=p.parse_args()
    df=fetch(a.query,a.limit); __import__("pathlib").Path(a.output).parent.mkdir(parents=True,exist_ok=True); df.to_csv(a.output,index=False); print("saved",len(df))
