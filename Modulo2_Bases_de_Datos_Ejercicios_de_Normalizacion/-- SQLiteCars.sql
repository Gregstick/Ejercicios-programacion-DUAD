-- SQLite

-- CREATE TABLE Owner (
--     Owner_id INT PRIMARY KEY,
--     Owner_name VARCHAR(25),
--     Owner_phone VARCHAR(20)
-- );

-- CREATE TABLE Insurance (
--     Insurance_id INT PRIMARY KEY,
--     Insurance_company VARCHAR(25),
--     Insurance_policy VARCHAR(8)
-- );

-- CREATE TABLE Cars (
--     Cars_id INT PRIMARY KEY,
--     VIN VARCHAR(15),
--     Make VARCHAR(20),
--     Model VARCHAR(20),
--     Year INT,
--     Color VARCHAR(25)
-- );


-- INSERT INTO Cars_owners(Cars_id, Year, Color, Owner_id, Insurance_id)
--     VALUES
--         (1, '2003', 'Silver',101, 123),
--         (1, '2007', 'Silver', 102, 456),
--         (2, '2014', 'Blue', 103, 789),
--         (3, '2015', 'Red', 104, 111);


-- INSERT INTO Cars(Cars_id, VIN, Make, Model, Year, Color)
--     VALUES
--         (1, 'IHGCM82633A', 'Honda', 'Accord', 2003, 'Silver'),
--         (2, '5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue'),
--         (3, '1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red');

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
