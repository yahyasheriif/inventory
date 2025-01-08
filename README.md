    Inventory Management System

    This project is an inventory management system built with Django and Django REST Framework. It allows users to manage inventory items, track changes, and handle user authentication and permissions.

    ## Features

    - User registration and authentication
    - CRUD operations for inventory items
    - Track changes in inventory quantities
    - Filter and order inventory items
    - Permissions to ensure only owners can edit their items

    ## Installation

    1. Clone the repository:
        ```bash
        git clone <repository_url>
        cd inventory
        ```

    2. Create and activate a virtual environment:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    3. Install the required packages:
        ```bash
        pip install -r requirements.txt
        ```

    4. Apply migrations:
        ```bash
        python manage.py migrate
        ```

    5. Create a superuser:
        ```bash
        python manage.py createsuperuser
        ```

    6. Run the development server:
        ```bash
        python manage.py runserver
        ```

    ## API Endpoints

    ### User Endpoints

    - `POST /api/users/`: Create a new user.
    - `GET /api/users/`: List all users.
    - `GET /api/users/{id}/`: Retrieve a user by ID.
    - `PUT /api/users/{id}/`: Update a user by ID.
    - `DELETE /api/users/{id}/`: Delete a user by ID.

    ### Inventory Item Endpoints

    - `GET /api/inventory/`: List all inventory items.
    - `POST /api/inventory/`: Create a new inventory item.
    - `GET /api/inventory/{id}/`: Retrieve an inventory item by ID.
    - `PUT /api/inventory/{id}/`: Update an inventory item by ID.
    - `DELETE /api/inventory/{id}/`: Delete an inventory item by ID.

    ### Inventory Change Log Endpoints

    - `GET /api/inventory-changes/`: List all inventory change logs.
    - `GET /api/inventory-changes/{id}/`: Retrieve an inventory change log by ID.

    ## Permissions

    - Only authenticated users can view and edit inventory items.
    - Only the owner of an inventory item can edit it.
    - Only authenticated users can view inventory change logs.

    ## Filtering and Ordering

    - Inventory items can be filtered by `category`, `price`, and `quantity`.
    - Inventory items can be ordered by `name`, `quantity`, `price`, and `date_added`.

    ## License

    This project is licensed under the MIT License.
