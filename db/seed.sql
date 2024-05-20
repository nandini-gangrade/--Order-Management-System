
-- Insert values into Product table
INSERT INTO Product (productId, productName, description, price, quantityInStock, type)
VALUES
    (1, 'Laptop', 'High-performance laptop for gaming and productivity', 1200.00, 50, 'Electronics'),
    (2, 'Smartphone', 'Latest smartphone with advanced features', 800.00, 100, 'Electronics'),
    (3, 'T-Shirt', 'Casual cotton T-shirt', 20.00, 200, 'Clothing'),
    (4, 'Jeans', 'Classic denim jeans', 50.00, 150, 'Clothing'),
    (5, 'TV', '55-inch smart TV with 4K resolution', 900.00, 30, 'Electronics'),
    (6, 'Sneakers', 'Sports sneakers for running and gym', 80.00, 100, 'Clothing'),
    (7, 'Headphones', 'Wireless headphones with noise cancellation', 150.00, 80, 'Electronics');

-- Insert values into Electronics table
INSERT INTO Electronics (productId, brand, warrantyPeriod)
VALUES
    (1, 'Dell', 2),
    (2, 'Samsung', 1),
    (3, 'Apple', 2),
    (4, 'HP', 1),
    (5, 'Sony', 3),
    (6, 'LG', 2),
    (7, 'Bose', 2);

-- Insert values into Clothing table
INSERT INTO Clothing (productId, size, color)
VALUES
    (1, 'M', 'Black'),
    (2, 'S', 'Blue'),
    (3, 'M', 'White'),
    (4, 'L', 'Red'),
    (5, 'XL', 'Green'),
    (6, 'S', 'Yellow'),
    (7, 'M', 'Purple')


-- Insert values into User table
INSERT INTO [User] (username, password, role)
VALUES
    ('admin', 'admin123', 'Admin'),
    ('user1', 'user123', 'User'),
    ('user2', 'user123', 'User'),
    ('user3', 'user123', 'User'),
    ('user4', 'user123', 'User'),
    ('user5', 'user123', 'User'),
    ('user6', 'user123', 'User');

-- Insert values into Order table
INSERT INTO [Order] (userId, status)
VALUES
    (2, 'Pending'),
    (3, 'Completed'),
    (4, 'Pending'),
    (2, 'Completed'),
    (5, 'Pending'),
    (6, 'Completed'),
    (7, 'Pending');

-- Insert values into OrderDetails table
INSERT INTO OrderDetails (orderId, productId, quantity)
VALUES
    (1, 1, 2),
    (2, 3, 1),
    (2, 4, 1),
    (3, 7, 1),
    (4, 2, 1),
    (5, 5, 1),
    (6, 6, 1),
    (7, 7, 1);
