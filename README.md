# 📚 Book Recommendation & Customer Intelligence Platform

> **An end-to-end Data Science, Machine Learning, NLP, and Business Intelligence platform for understanding customers, analyzing book performance, and delivering personalized book recommendations.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker)](https://www.docker.com/)

---

## 🚀 Project Overview

The **Book Recommendation & Customer Intelligence Platform** is an end-to-end analytics and machine learning project designed to simulate a real-world online bookstore intelligence system.

The platform combines:

* 📚 Book data ingestion
* 🧹 Data cleaning and validation
* 🗄️ SQL database design
* 📊 Business analytics
* 👥 Customer segmentation
* 🤖 Recommendation systems
* 💬 Review sentiment analysis
* 📈 Interactive dashboards
* 🧠 Optional AI-powered business analysis

The goal is not only to recommend books, but also to answer important business questions such as:

> **Who are our most valuable customers?**

> **Which books and genres generate the most revenue?**

> **Which customers are at risk of becoming inactive?**

> **What books should be recommended to a particular customer?**

> **How do customers feel about our books?**

> **What business actions should we take based on the data?**

---

# 🎯 Business Problem

A modern bookstore collects multiple types of information:

```text
Book Metadata
     ↓
Customer Activity
     ↓
Ratings & Reviews
     ↓
Purchases
     ↓
Wishlist / Views / Interactions
```

However, raw data alone does not provide useful business intelligence.

This project transforms that data into:

```text
Raw Data
   ↓
Data Quality & Cleaning
   ↓
SQL Analytics
   ↓
Customer Intelligence
   ↓
Recommendation Engine
   ↓
NLP & Sentiment Analysis
   ↓
Business Dashboard
   ↓
AI Business Analyst
```

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │  Open Library API   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      CSV Data       │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │ Validation & Data Cleaning│
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │      PostgreSQL DB       │
                 │                          │
                 │ Users                    │
                 │ Books                    │
                 │ Ratings                  │
                 │ Purchases                │
                 │ Reviews                  │
                 └────────────┬─────────────┘
                              │
             ┌────────────────┼─────────────────┐
             │                │                 │
             ▼                ▼                 ▼
       ┌───────────┐   ┌──────────────┐   ┌────────────┐
       │ Business  │   │ Customer     │   │ NLP /      │
       │ Analytics │   │ Intelligence │   │ Sentiment  │
       └─────┬─────┘   └──────┬───────┘   └─────┬──────┘
             │                │                 │
             │                ▼                 │
             │         ┌──────────────┐         │
             │         │ RFM + KMeans  │         │
             │         └──────┬───────┘         │
             │                │                 │
             └────────┬───────┼─────────────────┘
                      │       │
                      ▼       ▼
                ┌──────────────────────┐
                │ Recommendation Engine│
                │                      │
                │ Content-Based        │
                │ Collaborative        │
                │ Hybrid               │
                └──────────┬───────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Recommendation     │
                 │ Evaluation         │
                 │                    │
                 │ Precision@K        │
                 │ Recall@K           │
                 │ NDCG@K             │
                 └─────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Streamlit Dashboard │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ AI Business Analyst │
                └─────────────────────┘
```

---

# ✨ Main Features

## 1. 📚 Book Data Ingestion

The platform supports book metadata from:

* Open Library public API
* CSV datasets
* Processed project data

Example book attributes:

```text
Book ID
Title
Author
Genre
Publisher
Publication Date
Price
Rating
Review Count
Language
Description
```

The Open Library integration is implemented in:

```text
src/ingestion/openlibrary_client.py
```

---

# 2. 🧹 Data Cleaning & Validation

Before analytics and machine learning, the data goes through a validation pipeline.

The system checks for:

* Missing values
* Duplicate records
* Invalid ratings
* Invalid prices
* Incorrect data types
* Invalid customer/book references
* Data consistency

Validation reports are generated in:

```text
data/validation/
```

---

# 3. 🗄️ PostgreSQL Database

The project includes a relational database design for storing bookstore data.

### Main tables

```text
users
books
ratings
purchases
reviews
```

Database schema:

```text
sql/schema.sql
```

Business analysis queries:

```text
sql/business_queries.sql
```

Example business questions include:

* Top-selling books
* Revenue by genre
* Highest-value customers
* Customer purchase behavior
* Book popularity
* Rating performance

---

# 4. 👥 Customer Intelligence

Customer behavior is analyzed using **RFM analysis**.

### RFM

| Metric    | Meaning                               |
| --------- | ------------------------------------- |
| Recency   | How recently the customer purchased   |
| Frequency | How frequently the customer purchased |
| Monetary  | How much the customer spent           |

Customers are then segmented using **K-Means clustering**.

Example segments:

```text
Champions
Loyal Customers
Potential Loyalists
At Risk
New Customers
Low Value
```

Implementation:

```text
src/analytics/rfm.py
```

This allows businesses to identify:

* High-value customers
* Loyal customers
* Inactive customers
* Customers requiring re-engagement
* Potential high-value customers

---

# 5. 🤖 Recommendation System

The platform uses multiple recommendation approaches.

## Content-Based Recommendation

Books are represented using their textual metadata.

Features include:

```text
Title
Author
Genre
Description
```

TF-IDF is used to convert text into numerical vectors.

Cosine similarity is then used to identify similar books.

```text
Book A
  ↓
TF-IDF Vector
  ↓
Cosine Similarity
  ↓
Similar Books
```

Implementation:

```text
src/recommendation/content.py
```

---

## Collaborative Filtering

The system also learns from customer-book interactions.

Example:

```text
User A → Book 1 ⭐⭐⭐⭐⭐
User A → Book 2 ⭐⭐⭐⭐

User B → Book 1 ⭐⭐⭐⭐⭐
User B → Book 3 ⭐⭐⭐⭐⭐
```

The system can identify relationships between books based on customer behavior.

Implementation:

```text
src/recommendation/collaborative.py
```

---

## 🔀 Hybrid Recommendation

The platform combines recommendation signals from:

```text
Content-Based
      +
Collaborative Filtering
      ↓
Hybrid Recommendation
```

This provides a more balanced recommendation strategy by considering both:

* Book similarity
* Customer behavior

---

# 6. 📏 Recommendation Evaluation

Recommendation quality is evaluated using ranking metrics.

Implemented metrics include:

### Precision@5

Measures how many of the top 5 recommendations are relevant.

### Recall@5

Measures how many relevant items are successfully recommended.

### NDCG@5

Measures ranking quality while giving more importance to highly ranked relevant items.

Metrics are available in:

```text
src/recommendation/evaluation.py
```

Model results are stored in:

```text
data/processed/model_metrics.csv
```

---

# 7. 💬 NLP & Review Sentiment Analysis

Customer reviews are analyzed to understand customer opinions.

The NLP pipeline identifies:

```text
Positive Reviews
Negative Reviews
Neutral Reviews
```

This can help answer:

* Are customers satisfied?
* Which books receive negative feedback?
* Which books receive positive feedback?
* What areas may require improvement?

Implementation:

```text
src/nlp/sentiment.py
```

Processed sentiment results:

```text
data/processed/review_sentiment.csv
```

---

# 8. 📊 Interactive Streamlit Dashboard

The project includes a business dashboard built with Streamlit.

Run:

```powershell
streamlit run app.py
```

The dashboard provides sections for:

### Executive Dashboard

* Total customers
* Total books
* Total purchases
* Revenue
* Revenue by genre
* Customer segments

### Customer Intelligence

* Customer selection
* RFM information
* Customer behavior
* Recommendations

### Recommendations

* Personalized recommendations
* Collaborative recommendations
* Book similarity

### Reviews

* Sentiment distribution
* Review analysis
* Customer feedback

### AI Business Analyst

Ask natural-language business questions and receive analytical responses.

---

# 9. 🧠 AI Business Analyst

The project includes an optional LLM-powered business analyst.

The analyst can receive business context and answer questions such as:

```text
Which genre generates the highest revenue?

Which customer segment should we target?

What are the most popular books?

Which customers may need re-engagement?

What marketing strategy would you recommend?
```

The system supports an **OpenAI-compatible API endpoint**.

Configuration is available through:

```text
.env
```

Example:

```env
LLM_BASE_URL=
LLM_MODEL=
LLM_API_KEY=
```

Implementation:

```text
src/llm/business_analyst.py
```

---

# 📁 Project Structure

```text
book-recommendation-customer-intelligence/
│
├── app.py
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── books.csv
│   │
│   ├── processed/
│   │   ├── books_clean.csv
│   │   ├── users.csv
│   │   ├── ratings.csv
│   │   ├── purchases.csv
│   │   ├── interactions.csv
│   │   ├── reviews.csv
│   │   ├── rfm_segments.csv
│   │   ├── review_sentiment.csv
│   │   └── model_metrics.csv
│   │
│   └── validation/
│       └── book_data_quality_report.csv
│
├── src/
│   ├── analytics/
│   │   └── rfm.py
│   │
│   ├── cleaning/
│   │   └── validate.py
│   │
│   ├── ingestion/
│   │   └── openlibrary_client.py
│   │
│   ├── llm/
│   │   └── business_analyst.py
│   │
│   ├── nlp/
│   │   └── sentiment.py
│   │
│   ├── recommendation/
│   │   ├── content.py
│   │   ├── collaborative.py
│   │   └── evaluation.py
│   │
│   └── pipeline.py
│
├── sql/
│   ├── schema.sql
│   └── business_queries.sql
│
├── scripts/
│   └── build_demo_data.py
│
├── excel/
│   └── Book_Customer_Intelligence.xlsx
│
├── dashboard/
│   └── README.md
│
├── notebooks/
│   └── README.md
│
└── tests/
    ├── test_cleaning.py
    └── test_metrics.py
```

---

# ⚙️ Technology Stack

| Area               | Technology                                         |
| ------------------ | -------------------------------------------------- |
| Programming        | Python                                             |
| Data Analysis      | Pandas, NumPy                                      |
| Machine Learning   | Scikit-Learn                                       |
| Recommendation     | TF-IDF, Cosine Similarity, Collaborative Filtering |
| Customer Analytics | RFM, K-Means                                       |
| NLP                | Text Sentiment Analysis                            |
| Database           | PostgreSQL                                         |
| SQL                | PostgreSQL SQL                                     |
| Dashboard          | Streamlit                                          |
| Visualization      | Plotly                                             |
| API                | Open Library                                       |
| AI                 | OpenAI-compatible LLM                              |
| Containerization   | Docker                                             |
| Testing            | Pytest                                             |
| Excel              | OpenPyXL                                           |

---

# 🛠️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Rahulkumar65/book-recommendation-customer-intelligence.git
cd book-recommendation-customer-intelligence
```

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧪 Generate Demo Data

The project contains synthetic customer behavior for demonstration purposes.

Generate the dataset:

```bash
python scripts/build_demo_data.py
```

This generates the required datasets under:

```text
data/processed/
```

---

# 🔄 Run the Data Pipeline

Run:

```bash
python -m src.pipeline
```

The pipeline performs the project's analytical processing and generates the processed outputs.

---

# 📊 Start the Dashboard

Run:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in your terminal.

---

# 🐳 PostgreSQL with Docker

The project includes a Docker Compose configuration for PostgreSQL.

Start the database:

```bash
docker compose up -d
```

The database configuration is defined in:

```text
docker-compose.yml
```

Default development configuration:

```text
Database: bookintel
User: bookuser
Port: 5432
```

---

# 🧪 Run Tests

Run:

```bash
pytest -q
```

The project includes tests covering:

* Data cleaning
* Recommendation evaluation metrics

---

# 📊 Example Business Questions

The platform is designed to answer questions across several business areas.

## Customer Analytics

```text
Who are our highest-value customers?

Which customers are most loyal?

Which customers are becoming inactive?

Which customer segments should receive marketing campaigns?
```

## Product Analytics

```text
Which books are most popular?

Which genres generate the most revenue?

Which books have the highest ratings?

Which books receive the most reviews?
```

## Recommendation Analytics

```text
What should we recommend to this customer?

Which books are similar to this book?

How accurate is the recommendation system?

Which recommendation strategy performs best?
```

## Marketing Analytics

```text
Which customer segment should we target?

Which customers should receive re-engagement campaigns?

Which genres should be promoted?

Which books could be used for cross-selling?
```

## Customer Feedback

```text
Are customers generally satisfied?

Which books receive negative feedback?

Which books have the strongest customer sentiment?
```

---

# 📈 Business Value

This project demonstrates how multiple data disciplines can work together.

### Data Engineering

```text
API → Validation → Cleaning → Database
```

### Data Analytics

```text
SQL → KPIs → Customer/Product Analysis
```

### Customer Intelligence

```text
RFM → K-Means → Customer Segmentation
```

### Machine Learning

```text
TF-IDF
+
Collaborative Filtering
+
Hybrid Recommendations
```

### NLP

```text
Reviews → Sentiment → Customer Feedback Insights
```

### Business Intelligence

```text
Analytics → Dashboard → Business Decisions
```

### Generative AI

```text
Business Question
       ↓
AI Business Analyst
       ↓
Data Context
       ↓
Business Explanation
```

---

# 📋 Data Disclaimer

The customer behavior included in this repository is **synthetic demo data** created for development and demonstration.

It does not represent real customer transactions.

Book metadata can be refreshed using the Open Library public API.

---

# 🔮 Future Improvements

The platform can be extended with:

* [ ] Production-scale database ingestion
* [ ] Automated scheduled data pipelines
* [ ] Advanced hybrid recommendation algorithms
* [ ] MAP@K evaluation
* [ ] More advanced NLP topic extraction
* [ ] Review keyword analysis
* [ ] Real-time recommendation API
* [ ] FastAPI backend
* [ ] Authentication and user accounts
* [ ] Recommendation A/B testing
* [ ] Advanced Power BI dashboard
* [ ] Customer lifetime value prediction
* [ ] Churn prediction
* [ ] Demand forecasting
* [ ] Personalized marketing campaigns
* [ ] LLM-generated SQL analytics
* [ ] Automated business reports
* [ ] Cloud deployment

---

# 🎓 Skills Demonstrated

This project demonstrates practical experience with:

```text
Python
Pandas
NumPy
SQL
PostgreSQL
Data Cleaning
Data Validation
Exploratory Data Analysis
Business Analytics
RFM Analysis
K-Means Clustering
Recommendation Systems
TF-IDF
Cosine Similarity
Collaborative Filtering
NLP
Sentiment Analysis
Machine Learning Evaluation
Streamlit
Plotly
Docker
REST APIs
LLM Integration
Software Testing
Git & GitHub
```

---

# 👨‍💻 Project Purpose

This project was developed as a **portfolio-ready end-to-end data and machine learning application** demonstrating how raw business data can be transformed into actionable customer and product intelligence.

The focus is on connecting:

**Data → Analytics → Machine Learning → NLP → Business Intelligence → AI**

rather than treating each technology as an isolated exercise.

---

# ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational, portfolio, and demonstration purposes.

```markdown
[Open the Streamlit App](https://book-recommendation-customer-intelligence-84ftawbf6hxvsjmuvuc8.streamlit.app/)
