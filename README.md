# Django Products and Variants API

This is a Django-based API for bulk insertion of products and their variants. The project allows you to create products and their associated variants (such as different flavors or sizes) through an API endpoint.

## Features

- Bulk insert products and their variants
- Products can have multiple variants (e.g., a product like Yoghurt can have variants like Vanilla or Strawberry)
- Uses Django and Django REST Framework

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11.9 and above installed on your machine.
- `pip` installed (Python’s package installer).
- Virtual environment setup (recommended).
- Git for version control.
- Django version 5.1.2.
- Postman for API testing.


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/samuelcromwell/Interintel.git
cd interintel
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Run the following commands to apply migrations and set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Test the API using Postman
- Open Postman and create a new POST request.
- Set the request URL to: http://127.0.0.1:8000/api/products/bulk-create/.
- In the Body tab, select raw and then choose JSON format.
- Use the following sample JSON payload to bulk insert products and variants:

```bash
[
    {
        "name": "Yoghurt",
        "image": "yoghurt_image_url",
        "variants": [
            {
                "sku": "VAN123",
                "name": "Vanilla",
                "price": "1.99",
                "details": "Vanilla flavored yoghurt"
            },
            {
                "sku": "STW123",
                "name": "Strawberry",
                "price": "2.49",
                "details": "Strawberry flavored yoghurt"
            }
        ]
    },
    {
        "name": "Milk",
        "image": "milk_image_url",
        "variants": [
            {
                "sku": "MLK123",
                "name": "Whole Milk",
                "price": "1.50",
                "details": "Whole milk from organic farms"
            }
        ]
    }
]
```

# Author
Samuel Cromwell