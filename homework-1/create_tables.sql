-- SQL-команды для создания таблиц
CREATE TABLE employees(
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	title VARCHAR(100),
	birth_date DATE,
	bio TEXT
);
SELECT * FROM employees;

CREATE TABLE customers(
	customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    contact_name VARCHAR(100)
);
SELECT * FROM customers;

CREATE TABLE orders(
	order_id INTEGER,
    customer_id VARCHAR(255) REFERENCES customers(customer_id),
    employee_id INTEGER REFERENCES employees(employee_id),
    order_date DATE,
    ship_city VARCHAR(255)
);
SELECT * FROM orders;