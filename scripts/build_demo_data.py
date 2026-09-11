from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import random,numpy as np,pandas as pd
from src.cleaning.validate import validate_books,clean_books
random.seed(42); np.random.seed(42)
R=Path("data"); [ (R/x).mkdir(parents=True,exist_ok=True) for x in ["raw","processed","validation"]]
catalog=[
("B001","The Midnight Library","Matt Haig","Fiction","choices possibilities meaning"),
("B002","The Hobbit","J.R.R. Tolkien","Fantasy","adventure friendship courage"),
("B003","Pride and Prejudice","Jane Austen","Romance","relationships society impressions"),
("B004","Atomic Habits","James Clear","Self Help","habits improvement consistency"),
("B005","Sapiens","Yuval Noah Harari","History","human history civilization"),
("B006","The Alchemist","Paulo Coelho","Fiction","dreams purpose growth"),
("B007","Dune","Frank Herbert","Science Fiction","politics ecology survival"),
("B008","Educated","Tara Westover","Biography","education family transformation"),
("B009","Deep Work","Cal Newport","Productivity","focus work distraction"),
("B010","The Martian","Andy Weir","Science Fiction","science engineering survival"),
("B011","The Book Thief","Markus Zusak","Historical Fiction","books family wartime"),
("B012","Thinking Fast and Slow","Daniel Kahneman","Psychology","judgment decisions biases"),
("B013","Ikigai","Hector Garcia","Self Help","purpose routine meaning"),
("B014","The Name of the Wind","Patrick Rothfuss","Fantasy","music mystery adventure"),
("B015","Project Hail Mary","Andy Weir","Science Fiction","space science problem solving"),
("B016","Little Women","Louisa May Alcott","Fiction","family growth ambition"),
("B017","The Psychology of Money","Morgan Housel","Finance","wealth behavior decisions"),
("B018","Good Omens","Terry Pratchett & Neil Gaiman","Fantasy","humor unlikely allies"),
("B019","The Silent Patient","Alex Michaelides","Thriller","psychological mystery"),
("B020","The Alchemist's Garden","Demo Author","Fantasy","synthetic recommendation test")]
books=pd.DataFrame([{"book_id":b,"title":t,"author":a,"genre":g,"publisher":"Demo Publishing","publication_date":2000+i%25,"language":"en","description":d,"price":round(random.uniform(199,899),2),"rating":round(random.uniform(3.5,4.9),2),"review_count":random.randint(20,5000)} for i,(b,t,a,g,d) in enumerate(catalog)])
books.to_csv(R/"raw/books.csv",index=False); validate_books(books).to_csv(R/"validation/book_data_quality_report.csv",index=False); clean_books(books).to_csv(R/"processed/books_clean.csv",index=False)
users=pd.DataFrame({"user_id":range(1,251),"age_group":np.random.choice(["18-24","25-34","35-44","45-54","55+"],250),"country":np.random.choice(["India","UK","USA","Canada","Australia"],250,p=[.55,.1,.2,.08,.07]),"signup_date":pd.date_range("2024-01-01",periods=250,freq="2D").date}); users.to_csv(R/"processed/users.csv",index=False)
genres=books.genre.tolist(); interactions=[]; ratings=[]; purchases=[]; reviews=[]; iid=pid=rid=1; base=pd.Timestamp("2025-01-01")
templates=["Excellent and interesting read. I loved the story.","Great book with helpful ideas and an enjoyable narrative.","Interesting but the pacing was slow.","Confusing and disappointing in places.","Wonderful book. I enjoyed it and recommend it."]
for uid in users.user_id:
    fav=genres[(uid*7)%len(genres)]
    for bid in random.choices(books.book_id.tolist(),weights=[5 if g==fav else 1 for g in genres],k=random.randint(8,18)):
        dt=base+pd.Timedelta(days=random.randint(0,540),hours=random.randint(0,23)); r=round(float(np.clip(np.random.normal(4.1 if books.loc[books.book_id==bid,"genre"].iloc[0]==fav else 3.4,.7),1,5)),1)
        ratings.append({"user_id":uid,"book_id":bid,"rating":r,"timestamp":dt.isoformat()}); interactions.append({"interaction_id":iid,"user_id":uid,"book_id":bid,"interaction_type":"rating","timestamp":dt.isoformat()}); iid+=1
        if random.random()<.55:
            price=float(books.loc[books.book_id==bid,"price"].iloc[0]); purchases.append({"purchase_id":pid,"user_id":uid,"book_id":bid,"quantity":random.choice([1,1,1,2]),"price":price,"purchase_date":dt.isoformat()}); pid+=1
        if random.random()<.25: reviews.append({"review_id":rid,"user_id":uid,"book_id":bid,"review_text":random.choice(templates),"rating":r,"review_date":dt.isoformat()}); rid+=1
for n,rows in [("interactions",interactions),("ratings",ratings),("purchases",purchases),("reviews",reviews)]: pd.DataFrame(rows).drop_duplicates(["user_id","book_id"] if n=="ratings" else None).to_csv(R/"processed"/f"{n}.csv",index=False)
print("Created demo data:",len(books),"books,",len(users),"users,",len(ratings),"ratings,",len(purchases),"purchases")
