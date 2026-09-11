import pandas as pd
from src.cleaning.validate import clean_books
def test_clean():
 x=pd.DataFrame([{'book_id':'1','title':'A','author':'X'},{'book_id':'1','title':'dup','author':'X'},{'book_id':'2','title':'','author':'Y'}]); assert len(clean_books(x))==1
