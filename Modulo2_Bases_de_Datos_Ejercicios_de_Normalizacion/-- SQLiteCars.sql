-- SQLite

-- CREATE TABLE Owner (
--     Owner_id INT PRIMARY KEY,
--     Owner_name VARCHAR(25),
--     Owner_phone VARCHAR(20)
-- );

-- CREATE TABLE Insurance_company (
--     Insurance_id INT PRIMARY KEY,
--     Insurance_company VARCHAR(25)
-- );

-- CREATE TABLE Insurance_policy (
--     Policy_id INT PRIMARY KEY,
--     Insurance_id INT REFERENCES Insurance_company(Insurance_id),
--     Insurance_policy VARCHAR(8)
-- );

-- CREATE TABLE Car_model (
--     Model_id INT PRIMARY KEY,
--     Make VARCHAR(20),
--     Model VARCHAR(20),
--     Year INT
-- );

-- CREATE TABLE Car_unit (
--     Car_id INT PRIMARY KEY,
--     VIN VARCHAR(15),
--     Model_id INT REFERENCES Car_model(Model_id),
--     Color VARCHAR(25)
-- );

-- INSERT INTO Insurance_company(Insurance_id, Insurance_company)
--     VALUES
--         (1, 'ABC Insurance'),
--         (2, 'XYZ Insurance'),
--         (3, 'DEF Insurance'),
--         (4, 'GHI Insurance');


-- INSERT INTO Insurance_policy(Policy_id, Insurance_id, Insurance_policy)
--     VALUES
--         (1, 1, 'POL12345'),
--         (2, 2, 'POL54321'),
--         (3, 3, 'POL67890'),
--         (4, 4, 'POL98765');

-- INSERT INTO Cars_owners(Cars_id, Year, Color, Owner_id, Insurance_id)
--     VALUES
--         (1, '2003', 'Silver',101, 123),
--         (1, '2007', 'Silver', 102, 456),
--         (2, '2014', 'Blue', 103, 789),
--         (3, '2015', 'Red', 104, 111);


-- INSERT INTO Car_model(Model_id, Make, Model, Year)
--     VALUES
--         (1, 'Honda', 'Accord', 2003),
--         (2, 'Honda', 'CR-V', 2014),
--         (3, 'Chevrolet', 'Volt', 2015);

-- INSERT INTO Car_unit(Car_id, VIN, Model_id, Color)
--     VALUES
--         (1, 'IHGCM82633A', 1, 'Silver'),
--         (2, '5J6RM4H79EL', 2, 'Blue'),
--         (3, '1G1RA6EH1FU', 3, 'Red');

-- CREATE TABLE Car_Owner (
--     car_id INT,
--     owner_id INT,
--     insurance_id INT,
--     PRIMARY KEY (car_id, owner_id)
-- );


-- INSERT INTO Car_Owner (car_id, owner_id, insurance_id)
--     VALUES
--         (1, 101, 1),
--         (1, 102, 2),
--         (2, 103, 3),
--         (3, 104, 4);


