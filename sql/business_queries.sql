SELECT b.title,SUM(p.quantity) units FROM purchases p JOIN books b USING(book_id) GROUP BY b.book_id,b.title ORDER BY units DESC LIMIT 10;
SELECT b.genre,SUM(p.quantity*p.price) revenue FROM purchases p JOIN books b USING(book_id) GROUP BY b.genre ORDER BY revenue DESC;
SELECT user_id,SUM(quantity*price) revenue,COUNT(*) purchases FROM purchases GROUP BY user_id ORDER BY revenue DESC LIMIT 20;
