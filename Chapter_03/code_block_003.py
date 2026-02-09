Natural Language: "How many employees work in the marketing department?" SQL: SELECT COUNT(*) FROM employees WHERE department = 'marketing';
Natural Language: "Find the highest salary in the engineering department." SQL: SELECT MAX(salary) FROM employees WHERE department = 'engineering';
Prompt: "Translate the following question into an SQL query: 'Which products were sold in quantities greater than 100?'" The AI applies the patterns learned from the examples to generate the appropriate SQL query:
SELECT product_name FROM sales WHERE quantity_sold > 100;