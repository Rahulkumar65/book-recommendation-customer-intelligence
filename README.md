# 📚 Book Recommendation & Customer Intelligence Platform

A portfolio-ready end-to-end data/ML project combining data ingestion, validation, SQL, customer intelligence, recommendation systems, NLP, dashboards and an optional LLM analyst.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\build_demo_data.py
python -m src.pipeline
streamlit run app.py
```

The included customer behavior is **synthetic demo data** and is explicitly labeled as such. Book metadata can be refreshed from the Open Library public API.

## Main capabilities
- Open Library API ingestion
- Data cleaning and quality reporting
- PostgreSQL schema + business SQL
- RFM analysis and K-Means segmentation
- TF-IDF content recommendations
- Item-based collaborative filtering
- Hybrid recommendations
- Precision@5, Recall@5 and NDCG@5
- Review sentiment
- Streamlit business dashboard
- Optional OpenAI-compatible LLM Business Analyst
- Tests and Docker PostgreSQL

## Architecture

```text
API / CSV → Validation → Cleaning → PostgreSQL
                              ↓
              Customer + Transaction Analytics
                    ↓                 ↓
                 RFM/K-Means     Recommendation
                                      ↓
                         Content + Collaborative
                                      ↓
                                   Hybrid
                                      ↓
                         Evaluation + NLP
                                      ↓
                         Dashboard + LLM Analyst
```
