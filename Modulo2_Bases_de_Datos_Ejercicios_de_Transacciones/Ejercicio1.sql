CREATE TABLE users (
    user_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    stock INTEGER,
    price DECIMAL(10, 2)
);

CREATE TABLE invoices (
    invoice_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50) REFERENCES users(user_id),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE invoice_items (
    id SERIAL PRIMARY KEY,
    invoice_id VARCHAR(50) REFERENCES invoices(invoice_id),
    product_id VARCHAR(50) REFERENCES products(product_id),
    quantity INTEGER,
    subtotal DECIMAL(10, 2)
);

