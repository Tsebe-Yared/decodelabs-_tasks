-- Task 3: SQL Data Analysis

-- 1. Basic SELECT: view selected columns
SELECT "OrderID", "Product", "Quantity", "TotalPrice"
FROM orders;

-- 2. WHERE: filter for Cancelled orders
SELECT "OrderID", "Product", "OrderStatus", "TotalPrice"
FROM orders
WHERE "OrderStatus" = 'Cancelled';

-- 3. ORDER BY: top 10 highest-value orders
SELECT "OrderID", "Product", "TotalPrice"
FROM orders
ORDER BY "TotalPrice" DESC
LIMIT 10;

-- 4. GROUP BY + SUM/COUNT: total revenue and order count per product
SELECT "Product", SUM("TotalPrice") AS total_revenue, COUNT(*) AS order_count
FROM orders
GROUP BY "Product"
ORDER BY total_revenue DESC;

-- 5. AVG: average order value by payment method
SELECT "PaymentMethod", AVG("TotalPrice") AS avg_order_value, COUNT(*) AS order_count
FROM orders
GROUP BY "PaymentMethod"
ORDER BY avg_order_value DESC;

-- 6. WHERE + GROUP BY: revenue from Delivered orders only, by product
SELECT "Product", SUM("TotalPrice") AS delivered_revenue
FROM orders
WHERE "OrderStatus" = 'Delivered'
GROUP BY "Product"
ORDER BY delivered_revenue DESC;