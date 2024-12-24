# Recommendation Service

## Overview

This project provides a **Recommendation Service** built using **FastAPI**. It allows users to get personalized fashion recommendations with features like filtering, sorting, and pagination. Additionally, it supports event logging for user actions like clicks, which can be used for improving the recommendations.

---

## **Table of Contents**
1. [Tech Stack](#tech-stack)
2. [Setup Instructions](#setup-instructions)
    - [Clone the repository](#clone-the-repository)
    - [Create a virtual environment](#create-a-virtual-environment)
    - [Install dependencies](#install-dependencies)
    - [Run the application](#run-the-application)
3. [API Endpoints](#api-endpoints)
    - [GET /recommendations](#get-recommendations)
    - [POST /events](#post-events)
4. [Testing](#testing)
    - [Running Unit Tests](#running-unit-tests)
    - [Running Tests with Pytest](#running-tests-with-pytest)
5. [Troubleshooting](#troubleshooting)
6. [Future Enhancements](#future-enhancements)
7. [License](#license)

---

## **Tech Stack**
- **Backend Framework**: FastAPI
- **Programming Language**: Python
- **Testing Framework**: Pytest
- **Database**: In-memory simulation (can be replaced with an actual database for production)
- **API Testing**: Postman (or any HTTP client)

---

## **Setup Instructions**

### **1. Clone the repository**

Start by cloning the repository to your local system:

```bash
git clone https://github.com/your-repository/recommendation-service.git
cd recommendation-service
```
### **2. Create a virtual environment**

It's recommended to use a virtual environment to manage dependencies for your project:
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
### **3. Install dependencies**
Once inside the project folder and the virtual environment is activated, install the project dependencies:
```bash
pip install -r requirement.txt
```
The requirements.txt file should include all necessary dependencies like fastapi, uvicorn, pytest, etc.

### **4. Run the application**
To run the FastAPI application locally, use the following command:
```bash
uvicorn app.main:app --reload
```

The application will be available at [http://127.0.0.1:8000/docs].

## **API Endpoints**

# GET /recommendations

### Description:
Fetch personalized fashion recommendations with filters, sorting, and pagination.

### Query Parameters:

- `category` (optional): Filter items by category (e.g., Shirts).
- `price_min` (optional): Minimum price.
- `price_max` (optional): Maximum price.
- `size` (optional): Filter by size (e.g., L).
- `color` (optional): Filter by color (e.g., Red).
- `rating_min` (optional): Minimum rating.
- `sort_by` (optional): Sort by field (e.g., price, rating).
- `sort_order` (optional): Sort order (`asc` or `desc`).
- `page` (optional): Page number for pagination.
- `page_size` (optional): Number of items per page.

---

### Example Request:

```bash
curl -X GET "http://127.0.0.1:8000/recommendations?category=Shirts&price_min=20&price_max=100&sort_by=price&sort_order=asc&page=1&page_size=5"
```

### Example Response:

```bash
[
  {
    "id": "item_1",
    "name": "Casual Shirt",
    "category": "Shirts",
    "price": 25.0,
    "size": "M",
    "color": "Blue",
    "rating": 4.5
  }
]
```
# POST /events
### Description:
Logs user events such as clicks for recommendation analytics.

### Request Body:
```bash
{
  "user_id": "user123",
  "item_id": "item_1",
  "event_type": "click"
}
```
### Example Request:
```bash
curl -X POST "http://127.0.0.1:8000/events" -H "Content-Type: application/json" -d '{
  "user_id": "user123",
  "item_id": "item_1",
  "event_type": "click"
}'
```

### Example Response:

```bash
{
  "message": "Event recorded successfully"
}
```

# Testing

### Running Unit Tests
To test your application locally, the project includes unit tests that ensure the core functionality works as expected.

### **1. Run the tests using Pytest**
 - Install pytest
   ```bash
   pip install pytest
    ```

- To run all tests, execute the following command in the project root directory:

 ```bash
    pytest -v
 ```


