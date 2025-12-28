-- SQLite

-- CREATE TABLE Customer (
--     Customer_id INT PRIMARY KEY,
--     Customer_name VARCHAR(25) NOT NULL,
--     Customer_phone VARCHAR(20) NOT NULL
-- );


-- CREATE TABLE Address (
--     Address_id INT PRIMARY KEY,
--     Customer_id INT REFERENCES Customer(Customer_id),
--     Address VARCHAR(25)
-- );


-- CREATE TABLE Orders (
--     Order_id VARCHAR(3) PRIMARY KEY,
--     Customer_id INT REFERENCES Customer(Customer_id),
--     Address_id VARCHAR(25) REFERENCES Address(Address_id),
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

-- INSERT INTO Customer (Customer_id, Customer_name, Customer_phone)
--     VALUES 
--         (1, 'Alice', '123-456-7890'),
--         (2, 'Bob', '987-654-3210'),
--         (3, 'Claire', '555-123-4567');


-- INSERT INTO Address (Address_id, Customer_id, Address)
--     VALUES
--         (1, 1, '123 Main Str'),
--         (2, 2, '456 Elm Str'),
--         (3, 3, '789 Oak Str'),
--         (4, 3, '464 Georgia St');


-- INSERT INTO Orders (Order_id, Customer_id, Address_id, Delivery_item)
--     VALUES
--         ('001', 1, 1, '6:00 PM'),
--         ('002', 2, 2, '7:30 PM'),
--         ('003', 3, 3, '12:00 PM'),
--         ('004', 3, 4, '5:00 PM');


-- INSERT INTO Order_details (Order_id, Item_id, Quantity, Special_request)
--     VALUES
--         ('001', 101, 2, 'No Onions'),
--         ('001', 102, 1, 'Extra Ketchup'),
--         ('002', 103, 1, 'Extra Cheese'),
--         ('002', 104, 2, 'None'),
--         ('003', 105, 1, 'No Crutons'),
--         ('004', 106, 1, 'None');
