CREATE TABLE users(user_id INT PRIMARY KEY,age_group VARCHAR(30),country VARCHAR(80),signup_date DATE);
CREATE TABLE books(book_id VARCHAR(50) PRIMARY KEY,title VARCHAR(500) NOT NULL,author VARCHAR(300),genre VARCHAR(100),publisher VARCHAR(300),publication_date INT,language VARCHAR(30),description TEXT,price NUMERIC(10,2),rating NUMERIC(3,2),review_count INT);
CREATE TABLE ratings(user_id INT,book_id VARCHAR(50),rating NUMERIC(2,1),timestamp TIMESTAMP);
CREATE TABLE purchases(purchase_id BIGINT PRIMARY KEY,user_id INT,book_id VARCHAR(50),quantity INT,price NUMERIC(10,2),purchase_date TIMESTAMP);
CREATE TABLE reviews(review_id BIGINT PRIMARY KEY,user_id INT,book_id VARCHAR(50),review_text TEXT,rating NUMERIC(2,1),review_date TIMESTAMP);
