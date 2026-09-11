import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
class ItemCollaborativeRecommender:
    def fit(self,ratings):
        self.matrix=ratings.pivot_table(index="user_id",columns="book_id",values="rating",aggfunc="mean").fillna(0)
        self.sim=cosine_similarity(self.matrix.T); self.items=self.matrix.columns.tolist(); return self
    def recommend(self,user_id,k=10):
        if user_id not in self.matrix.index:return []
        u=self.matrix.loc[user_id].values; scores=np.zeros(len(self.items))
        for i,r in enumerate(u):
            if r>0:scores+=r*self.sim[:,i]
        seen=set(self.matrix.loc[user_id][self.matrix.loc[user_id]>0].index)
        return [self.items[i] for i in np.argsort(-scores) if self.items[i] not in seen][:k]
