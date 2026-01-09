-- SQLite

-- CREATE TABLE Authors (
--     Author_id INT PRIMARY KEY,
--     Name VARCHAR(25)
-- );

-- CREATE TABLE Books (
--     Books_id INT PRIMARY KEY,
--     Name VARCHAR(25),
--     Author INT REFERENCES Authors(Author_id)
-- );

-- CREATE TABLE Customers (
--     Customer_id INT PRIMARY KEY,
--     Name VARCHAR(25),
--     Email VARCHAR(35)
-- );

-- CREATE TABLE Rents (
--     Rent_id INT PRIMARY KEY,
--     Books_id INT REFERENCES Books(Books_id),
--     Customer_id INT REFERENCES Customers(Customer_id),
--     State VARCHAR(15)
-- );

-- INSERT INTO Authors (Author_id, Name)
--     VALUES
--         (1, 'Miguel de Cervantes'),
--         (2, 'Dante Alighieri'),
--         (3, 'Takehiko Inoue'),
--         (4, 'Akira Toriyama'),
--         (5, 'Walt Disney');

-- INSERT INTO Books (Books_id, Name, Author)
--     VALUES
--         (1, 'Don Quijote', 1),
--         (2, 'La Divina Comedia', 2),
--         (3, 'Vagabond 1-3', 3),
--         (4, 'Dragon Ball 1', 4),
--         (5, 'The Book of the 5 Rings', NULL);

-- INSERT INTO Customers (Customer_id, Name, Email)
--     VALUES
--         (1, 'John Doe', 'j.doe@email.com'),
--         (2, 'Jane Doe', 'jane@doe.com'),
--         (3, 'Luke Skywalker', 'darth.son@email.com');


-- INSERT INTO Rents (Rent_id, Books_id, Customer_id, State)
--     VALUES
--         (1, 1, 2, 'Returned'),
--         (2, 2, 2, 'Returned'),
--         (3, 1, 1, 'On time'),
--         (4, 3, 1, 'On time'),
--         (5, 2, 2, 'Overdue');


-- SELECT Books.Name, Authors.Name
-- FROM Books AS Books
-- INNER JOIN Authors AS Authors
-- ON Books.Books_id = Authors.Author_id


-- SELECT
-- Books.Name AS book_name,
-- Authors.Name AS author_name
-- FROM Books
-- LEFT JOIN Authors
-- ON Books.author = Authors.author_id;


-- SELECT
-- Authors.name AS author_name,
-- Books.name AS books_name
-- FROM Authors
-- LEFT JOIN Books
-- ON Authors.author_id = Books.author
-- WHERE Books.books_id IS NULL;


-- SELECT DISTINCT
-- Books.Books_id,
-- Books.Name
-- FROM Books
-- INNER JOIN Rents
-- ON Books.Books_id = Rents.Books_id;


-- SELECT
-- Books.Books_id,
-- Books.Name
-- FROM Books
-- LEFT JOIN Rents
-- ON Books.Books_id = Rents.Books_id
-- WHERE Rents.Books_id IS NULL;

-- SELECT
-- Customers.Customer_id,
-- Customers.Name,
-- Customers.Email
-- FROM Customers
-- LEFT JOIN Rents
-- ON Customers.Customer_id = Rents.Customer_id
-- WHERE Rents.Customer_id IS NULL;


-- SELECT DISTINCT
-- Books.Books_id,
-- Books.Name
-- FROM Books
-- INNER JOIN Rents
-- ON Books.Books_id = Rents.Books_id
-- WHERE Rents.State = 'Overdue';
