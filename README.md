# Django Project Setup Guide

## 🏗️ Create a Virtual Environment

```bash
python -m venv venv
```

## 🔥 Activate the Virtual Environment

### On Windows:
```bash
venv\Scripts\activate
```

### On macOS/Linux:
```bash
source venv/bin/activate
```

## 🔥 Clone the Repository

```bash
# Replace <repo-url> with your GitHub repository URL
git clone <repo-url>
cd tiket
```

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔄 Apply Migrations

```bash
python manage.py migrate
```

## 👤 Create Superuser

```bash
python manage.py createsuperuser
```

## 🏃 Run the Server

```bash
python manage.py runserver
```

## 📡 API Endpoints

### 1️⃣ Create a Task (POST Method)

```bash
# API Endpoint
http://127.0.0.1:8000/api/tasks
```

**Request Body (JSON format):**
```json
{
    "id": 1,
    "description": "Task description here",
    "users": ["example1@gmail.com", "example2@gmail.com"],
    "status": "pending",
    "task_type": "feature"
}
```

**Response:**
- Status: `201 Created`
- Returns the created task object details.

---

### 2️⃣ Assign a Task to a User (PATCH Method)

```bash
# API Endpoint (Replace `id` with the task ID)
http://127.0.0.1:8000/api/tasks/id/
```

**Request Body (JSON format):**
```json
{
    "users": ["example1@gmail.com", "example2@gmail.com"]
}
```

**Response:**
- Status: `202 Accepted`
- Returns the updated task object details.

---

### 3️⃣ Fetch All Tasks Assigned to a Particular User (GET Method)

```bash
# API Endpoint (Pass user_email as a query parameter)
http://127.0.0.1:8000/api/tasks?user_email=example1@gmail.com
```

**Response:**
- Status: `200 OK`
- Returns all tasks related to the specified user.

---

## 🔑 Credentials

### Superuser
- **Email:** `admin.dev@gmail.com`
- **Password:** `admin`

### Second User
- **Email:** `mofafu@gmail.com`

## 📝 Note:
I have added my Postman test and response export with this repository. You can import it into your Postman setup and test all the API endpoints easily.
