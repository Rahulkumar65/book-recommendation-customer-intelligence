import math
def precision_at_k(rec,rel,k=5): return sum(x in rel for x in rec[:k])/max(1,k)
def recall_at_k(rec,rel,k=5): return sum(x in rel for x in rec[:k])/len(rel) if rel else 0
def ndcg_at_k(rec,rel,k=5):
    dcg=sum(1/math.log2(i+2) for i,x in enumerate(rec[:k]) if x in rel)
    ideal=sum(1/math.log2(i+2) for i in range(min(k,len(rel))))
    return dcg/ideal if ideal else 0
