-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(15) NOT NULL,
	last_name varchar(15) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date NOT NULL,
	notes varchar(1000) NOT NULL
);

SELECT * FROM employees;

CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

SELECT * FROM customers;

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(15) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(50) NOT NULL
);

SELECT * FROM orders;