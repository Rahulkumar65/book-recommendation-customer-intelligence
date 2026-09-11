from src.recommendation.evaluation import *
def test_metrics():
 r=['A','B','C','D','E']; rel={'B','D'}
 assert precision_at_k(r,rel)==.4
 assert recall_at_k(r,rel)==1
 assert ndcg_at_k(r,rel)>0
