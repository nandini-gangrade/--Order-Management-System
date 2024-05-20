CREATE DATABASE Order_Management_System

USE Order_Management_System

CREATE TABLE [Product] (
    productId INT PRIMARY KEY,
    productName NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX),
    price DECIMAL(10, 2) NOT NULL,
    quantityInStock INT NOT NULL,
    type NVARCHAR(50) CHECK (type IN ('Electronics', 'Clothing')) NOT NULL
);

CREATE TABLE [Electronics] (
    productId INT PRIMARY KEY,
    brand NVARCHAR(255),
    warrantyPeriod INT,
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

CREATE TABLE [Clothing] (
    productId INT PRIMARY KEY,
    size NVARCHAR(50),
    color NVARCHAR(50),
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

CREATE TABLE [User] (
    userId INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(255) NOT NULL UNIQUE,
    password NVARCHAR(255) NOT NULL,
    role NVARCHAR(50) CHECK (role IN ('Admin', 'User')) NOT NULL
);

CREATE TABLE [Order] (
    orderId INT PRIMARY KEY IDENTITY(1,1),
    userId INT NOT NULL,
    orderDate DATETIME NOT NULL DEFAULT GETDATE(),
    status NVARCHAR(50) NOT NULL,
    FOREIGN KEY (userId) REFERENCES [User](userId)
);

CREATE TABLE OrderDetails (
    orderDetailId INT PRIMARY KEY IDENTITY(1,1),
    orderId INT NOT NULL,
    productId INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (orderId) REFERENCES [Order](orderId),
    FOREIGN KEY (productId) REFERENCES Product(productId)
);
