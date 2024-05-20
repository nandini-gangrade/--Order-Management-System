
# Order Management System

The Order Management System is a Python-based application designed to manage orders, users, and products within a business environment. 
The Order Management System simplifies the process of managing orders and inventory for businesses. It allows users to interact with the system through a command-line interface (CLI), providing a straightforward way to perform various operations related to orders, users, and products.

## Features

- **User Management**: Create, modify, and delete user accounts with different roles (e.g., admin, regular user).
- **Product Management**: Add, update, and remove products from the inventory, including details such as name, description, price, and quantity.
- **Order Placement**: Place orders for products, specifying the quantity required.
- **Order Cancellation**: Cancel existing orders based on user input.
- **Data Retrieval**: Retrieve information about products and orders, such as product details, order status, and order history.

## How to Run

To run the Order Management System, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/nandini-gangrade/Order-Management-System.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Order-Management-System
   ```

3. (Optional but recommended) Create a virtual environment:

   ```bash
   python -m venv myenv
   ```

4. Activate the virtual environment:

   On Windows (PowerShell):

   ```powershell
   Set-ExecutionPolicy -Scope Process Bypass
   .\myenv\Scripts\Activate.ps1
   ```

   On Unix or MacOS:

   ```bash
   source myenv/bin/activate
   ```

5. Install the required dependencies:

   ```bash
   pip install pyodbc
   ```

6. Run the main.py file to start the application:

   ```bash
   python main.py
   ```

7. Follow the on-screen prompts to interact with the Order Management System.
