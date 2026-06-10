
INSERT INTO public.expenses (title, amount, category, expense_date)
VALUES ('Coffee', 4.50, 'Food', '2026-06-10');


UPDATE public.expenses
SET amount = 5.00
WHERE id = 1;


DELETE FROM public.expenses
WHERE id = 1;


SELECT *
FROM public.expenses
ORDER BY amount DESC;

SELECT COUNT(*) AS total_records
FROM public.expenses;