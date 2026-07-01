-- Query 1 — Top 5 Funds by AUM
SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM "03_aum_by_fund_house"
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

--Query 2 — Average NAV Per Month
SELECT
DATE_TRUNC('month', date) AS month,
ROUND(AVG(nav::numeric),2) AS average_nav
FROM "02_nav_history"
GROUP BY month
ORDER BY month;

--Query 3 — Transactions by State
SELECT
state,
COUNT(*) AS total_transactions,
SUM(amount) AS total_amount
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_amount DESC;

--Query 4 — Funds having Expense Ratio less than 1%
SELECT
scheme_name,
fund_house,
expense_ratio_pct
FROM "01_fund_master"
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

--Query 5 — Category Wise Average NAV
SELECT
fm.category,
ROUND(AVG(nh.nav::numeric),2) AS average_nav
FROM "02_nav_history" nh
JOIN "01_fund_master" fm
ON nh.amfi_code = fm.amfi_code
GROUP BY fm.category
ORDER BY average_nav DESC;

--Query 6 — Top Fund Houses by Number of Schemes
SELECT
fund_house,
COUNT(*) AS total_schemes
FROM "01_fund_master"
GROUP BY fund_house
ORDER BY total_schemes DESC;

--Query 6 — Top Fund Houses by Number of Schemes
SELECT
fund_house,
COUNT(*) AS total_schemes
FROM "01_fund_master"
GROUP BY fund_house
ORDER BY total_schemes DESC;

--Query 8 — States having investment greater than 10 Lakhs
SELECT
state,
SUM(amount) AS total_amount
FROM "08_investor_transactions"
GROUP BY state
HAVING SUM(amount) > 1000000
ORDER BY total_amount DESC;

--Query 9 — Fund having Highest NAV
SELECT
scheme_name,
nav
FROM "02_nav_history" nh
JOIN "01_fund_master" fm
ON nh.amfi_code = fm.amfi_code
WHERE nav = (
SELECT MAX(nav)
FROM "02_nav_history"
);

--Query 10 — Transaction Status using CASE WHEN
SELECT
investor_id,
amount,
CASE
WHEN amount >= 100000 THEN 'High Investment'
WHEN amount >= 50000 THEN 'Medium Investment'
ELSE 'Low Investment'
END AS investment_category
FROM "08_investor_transactions";