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
### **2. Create a virtual environment **

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
### ** 3. Install dependencies **
Once inside the project folder and the virtual environment is activated, install the project dependencies:
```bash
pip install -r requirements.txt
```
The requirements.txt file should include all necessary dependencies like fastapi, uvicorn, pytest, etc.

### **4. Run the application**
To run the FastAPI application locally, use the following command:
```bash
uvicorn app.main:app --reload
```

The application will be available at [http://127.0.0.1:8000/docs].
