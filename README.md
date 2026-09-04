# 🍹 Energy Drinks API

A simple and powerful REST API to manage a list of drinks, built with Flask.

## 📋 About the Project

This is a Flask application that provides endpoints to create, read, update, and delete drinks from an in-memory database. Perfect for learning about REST APIs and how to work with HTTP methods.

## 🚀 Features

- ✅ **GET** - List all drinks
- ✅ **GET** - Fetch drink by ID
- ✅ **POST** - Create new drink
- ✅ **PUT** - Update existing drink
- ✅ **DELETE** - Remove drink

## 📦 Prerequisites

- Python 3.7+
- pip (Python package manager)

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/LorenzoNeves/Energy_Drinks_API.git
cd Energy_Drinks_API
```

### 2. Create a virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ How to Run

```bash
python app.py
```

The API will be available at: `http://localhost:5000`

## 📡 Endpoints

### 1. List all drinks
```http
GET /drinks
```
**Response:**
```json
[
  {
    "id": 1,
    "name": "Monster",
    "price": "3.9$"
  },
  {
    "id": 2,
    "name": "Redbull",
    "price": "2$"
  }
]
```

---

### 2. Get drink by ID
```http
GET /drinks/1
```
**Response:**
```json
{
  "id": 1,
  "name": "Monster",
  "price": "3.9$"
}
```

---

### 3. Create new drink
```http
POST /drinks
Content-Type: application/json

{
  "id": 4,
  "name": "Guaraná",
  "price": "1.5$"
}
```
**Response:**
```json
{
  "id": 4,
  "name": "Guaraná",
  "price": "1.5$"
}
```

---

### 4. Update drink
```http
PUT /drinks/1
Content-Type: application/json

{
  "price": "4.5$"
}
```
**Response:**
```json
{
  "id": 1,
  "name": "Monster",
  "price": "4.5$"
}
```

---

### 5. Delete drink
```http
DELETE /drinks/1
```
**Response:**
```json
{
  "message": "Drink deleted",
  "drink": {
    "id": 1,
    "name": "Monster",
    "price": "3.9$"
  }
}
```

---

## 🧪 Testing with Postman

⚠️ **IMPORTANT:** To use POST, PUT, and DELETE functionalities, **you MUST use Postman** (or similar tools like curl, Insomnia, etc). Your web browser can only perform GET requests easily.

**Postman** is an excellent tool for testing APIs. Here's how to test this API:

### Installation
1. Download Postman from [postman.com](https://www.postman.com/downloads/)
2. Create a free account and install the application

### Testing the Endpoints

#### 1. GET - List all drinks
- **Method:** GET
- **URL:** `http://localhost:5000/drinks`
- **Click:** Send
- **Expected:** List of all drinks

#### 2. GET - Get drink by ID
- **Method:** GET
- **URL:** `http://localhost:5000/drinks/1`
- **Click:** Send
- **Expected:** Single drink with ID 1

#### 3. POST - Create new drink
- **Method:** POST
- **URL:** `http://localhost:5000/drinks`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
  "id": 4,
  "name": "Guaraná",
  "price": "1.5$"
}
```
- **Click:** Send
- **Expected:** New drink created

#### 4. PUT - Update drink
- **Method:** PUT
- **URL:** `http://localhost:5000/drinks/1`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
  "price": "4.5$"
}
```
- **Click:** Send
- **Expected:** Drink updated with new price

#### 5. DELETE - Remove drink
- **Method:** DELETE
- **URL:** `http://localhost:5000/drinks/1`
- **Click:** Send
- **Expected:** Drink deleted successfully

### Tips for Postman
- 💡 Save each endpoint as a "request" in Postman
- 💡 Create a "Collection" to organize all requests
- 💡 Use **Postman Environments** to change variables (like the base URL)
- 💡 Check the response status code (200, 201, 404, etc)
- 💡 View the response time and size

### Alternative: Using curl in terminal
If you prefer the command line:

```bash
# GET
curl http://localhost:5000/drinks

# POST
curl -X POST http://localhost:5000/drinks \
  -H "Content-Type: application/json" \
  -d '{"id": 4, "name": "Guaraná", "price": "1.5$"}'

# PUT
curl -X PUT http://localhost:5000/drinks/1 \
  -H "Content-Type: application/json" \
  -d '{"price": "4.5$"}'

# DELETE
curl -X DELETE http://localhost:5000/drinks/1
```

## 📁 Project Structure

```
drinks-api/
├── main.py           # Main application file
├── requirements.txt  # Project dependencies
└── README.md         # This file
```

## 🛠️ Technologies Used

- **Framework:** Flask
- **Language:** Python
- **Server:** Flask built-in development server

## 📝 Drink Structure

```json
{
  "id": 1,
  "name": "Drink Name",
  "price": "Price$"
}
```
