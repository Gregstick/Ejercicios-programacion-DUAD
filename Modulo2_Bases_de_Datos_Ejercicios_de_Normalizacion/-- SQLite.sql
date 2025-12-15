-- SQLite

-- CREATE TABLE Customer (
--     Customer_id INT PRIMARY KEY,
--     Customer_name VARCHAR(25) NOT NULL,
--     Customer_phone VARCHAR(20) NOT NULL,
--     Address VARCHAR(15)
-- );

-- CREATE TABLE Orders (
--     Order_id VARCHAR(3) PRIMARY KEY,
--     Customer_id INT REFERENCES Customer(Customer_id),
--     Delivery_item TEXT
-- );

-- CREATE TABLE Items (
--     Item_id INT(3) PRIMARY KEY,
--     Item_name VARCHAR,
--     Price TEXT
-- );

-- CREATE TABLE Order_details (
--     Order_id VARCHAR(3) REFERENCES Orders(Order_id),
--     Item_id VARCHAR(3) REFERENCES Items(Item_id),
--     Quantity INT,
--     Special_request VARCHAR(25),
--     PRIMARY KEY (Order_id, Item_id)
-- );

-- INSERT INTO CUSTOMER (Customer_id, Customer_name, Customer_phone, Address)
--     VALUES 
--         (1, 'Alice', 123-456-7890, '123 Main Str'),
--         (2, 'Bob', 987-654-3210, '456 Elm Str'),
--         (3, 'Claire', 555-123-4567, '789 Oak Str');

-- INSERT INTO Customer (Customer_id, Customer_name, Customer_phone, Address)
--     VALUES
--         (1, 'Alice', '123-456-7890', '123 Main Str'),
--         (2, 'Bob', '987-654-3210', '456 Elm Str'),
--         (3, 'Claire', '555-123-4567', '789 Oak Str');




