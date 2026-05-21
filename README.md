# Ecommerce Django Project

A Django-based ecommerce web application with category browsing, product details, cart/checkout flow, and basic account authentication.

## Tech Stack
- Python
- Django 5.2.x
- SQLite (default database)
- `django-crispy-forms` + `crispy-bootstrap5`

## Main Features
- Browse product categories.
- View products in a selected category.
- View detailed product pages.
- Add products to cart and manage cart items.
- Checkout and payment success flow.
- User registration, login, and logout.
- Admin-only pages for adding categories, products, and updating stock.

## Shop Views (from `Shop/views.py`)
- `CategoryView`: Loads all categories and renders `shop/category.html`.
- `ProductView`: Loads a category by ID and renders `shop/products.html`.
- `ProductDetailsView`: Loads a product by ID and renders `shop/product-details.html`.
- `AddCategoryView` (admin protected): Adds new categories with image upload support.
- `AddProductView` (admin protected): Adds new products with file upload support.
- `AddProductStockView` (admin protected): Updates stock for a product.
- `admin_required` decorator: Restricts selected class-based views to authenticated superusers.

## URL Overview
- `/` -> category listing (`Shop`)
- `/products/<cat_id>/` -> products by category (`Shop`)
- `/product-details/<pro_id>/` -> product details (`Shop`)
- `/add-category/` -> add category (admin only)
- `/add-product/` -> add product (admin only)
- `/add-stock/<pro_id>/` -> update stock (admin only)
- `/accounts/register/`, `/accounts/login/`, `/accounts/logout/`
- `/cart/add-to-cart/<pro_id>/`, `/cart/cart-view/`, checkout/order routes
- `/admin/` -> Django admin

## Project Setup
1. Clone the repository:
```bash
git clone <your-repo-url>
cd Ecommerce_P
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install django django-crispy-forms crispy-bootstrap5
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create an admin user:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Notes
- Media files are served from `/media/` in debug mode.
- Static assets are stored under `static/`.
- Default database file is `db.sqlite3`.
