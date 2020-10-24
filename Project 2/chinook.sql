-- Which tracks appeared in the most playlists? how many playlists did they appear in?
SELECT tracks.Name AS 'Track', COUNT(*) AS 'Playlist Count'
FROM tracks
JOIN playlist_track
ON tracks.TrackID = playlist_track.TrackId
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;

-- Which track generated the most revenue?
SELECT tracks.Name, SUM(invoice_items.UnitPrice) AS 'Total'
FROM tracks
JOIN invoice_items
ON tracks.TrackId = invoice_items.TrackId
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
-- which album?
SELECT albums.Title, SUM(invoice_items.UnitPrice) AS 'Total'
FROM albums
JOIN tracks
ON albums.AlbumId = tracks.AlbumId
JOIN invoice_items
ON tracks.TrackId = invoice_items.TrackId
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
-- which genre?
SELECT genres.Name, ROUND(SUM(invoice_items.UnitPrice),2) AS 'Total'
FROM genres
JOIN tracks
ON genres.GenreId = tracks.GenreId
JOIN invoice_items
ON tracks.TrackId = invoice_items.TrackId
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;

-- Which countries have the highest sales revenue? What percent of total revenue does each country make up?
SELECT BillingCountry AS 'Country', ROUND(SUM(Total),2) AS 'Total', ROUND(SUM(Total) * 100 / (SELECT SUM(Total) FROM invoices),1) AS '%'
FROM invoices
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10; 

-- How many customers did each employee support, what is the average revenue for each sale, and what is their total sale?
SELECT employees.FirstName || ' ' || employees.LastName AS 'Employee',
	COUNT(*) AS 'Customer Count',
	ROUND(AVG(invoices.Total),2) AS 'Average Revenue',
	ROUND(SUM(invoices.Total),2) AS 'Total'
FROM customers
JOIN employees
ON customers.SupportRepId = employees.EmployeeId
JOIN invoices
ON customers.CustomerId = invoices.CustomerId
GROUP BY 1;

-- Do longer or shorter length albums tend to generate more revenue?
WITH track_count AS (
	SELECT albums.AlbumId, COUNT(*) AS 'Count'
	FROM tracks
	JOIN albums
	ON tracks.AlbumId = albums.AlbumId
	GROUP BY 1
)
SELECT albums.Title, track_count.Count, SUM(invoice_items.UnitPrice) AS 'Total'
FROM albums
JOIN track_count
ON albums.AlbumId = track_count.AlbumId
JOIN tracks
ON albums.AlbumId = tracks.AlbumId
JOIN invoice_items
ON tracks.TrackId = invoice_items.TrackId
GROUP BY 1
ORDER BY 3 DESC
LIMIT 10;

-- Is the number of times a track appears in any playlist a good indicator of sales?
WITH playlist_track_count AS (
	SELECT TrackId, COUNT(*) AS 'Count'
	FROM playlist_track
	GROUP BY 1
), track_name AS (
	SELECT TrackId, Name
	FROM tracks
	ORDER BY 1
), total_revenue AS (
	SELECT TrackId, SUM(UnitPrice) AS 'Total'
	FROM invoice_items
	GROUP BY 1
)
SELECT track_name.TrackId AS 'Id', track_name.Name, playlist_track_count.Count, total_revenue.Total
FROM playlist_track_count
JOIN track_name
ON playlist_track_count.TrackId = track_name.TrackId
JOIN total_revenue
ON playlist_track_count.TrackId = total_revenue.TrackId
GROUP BY 1
ORDER BY 3 DESC;

-- How much revenue is generated each year, and what is its percent change from the previous year?
WITH revenue AS (
	SELECT CAST(strftime('%Y',InvoiceDate) AS INT) AS 'Year',
		CAST(strftime('%Y',InvoiceDate) AS INT) - 1 AS 'PrevYear',
		SUM(Total) AS 'TotalRevenue'
	FROM invoices
	GROUP BY 1
	ORDER BY 1 DESC
)
SELECT new.Year,
	new.PrevYear, 
	new.TotalRevenue, 
	ROUND(((new.TotalRevenue - old.TotalRevenue) / old.TotalRevenue) * 100, 2) AS 'Percent Change'
FROM revenue new
LEFT JOIN revenue old
ON new.PrevYear = old.Year;