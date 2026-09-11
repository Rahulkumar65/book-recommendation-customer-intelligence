import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class ContentRecommender:
    def fit(self,books):
        self.books=books.reset_index(drop=True).copy()
        cols=["title","author","genre","description"]
        text=self.books[cols].fillna("").agg(" ".join,axis=1)
        self.similarity=cosine_similarity(TfidfVectorizer(stop_words="english",ngram_range=(1,2)).fit_transform(text))
        return self
    def recommend(self,book_id,k=10):
        hit=self.books.index[self.books.book_id==book_id].tolist()
        if not hit:return self.books.head(0)
        i=hit[0]; order=np.argsort(-self.similarity[i]); order=[j for j in order if j!=i][:k]
        return self.books.iloc[order]
