SELECT * FROM public.expenses;

SELECT *
FROM public.expenses
WHERE category = 'Food';

SELECT SUM(amount) AS total_expenses
FROM public.expenses;

SELECT category,
       SUM(amount) AS category_total
FROM public.expenses
GROUP BY category;