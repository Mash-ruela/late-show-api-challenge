# 🎤 Late Show API

A RESTful API built with **Flask** and **PostgreSQL** to manage talk show guests, episodes, and appearances. Includes JWT-based authentication and protected routes.

---

## 🚀 Setup Instructions

### ✅ Prerequisites

- Python 3.12+
- PostgreSQL installed and running
- Pipenv installed (`pip install pipenv`)

---

### 📦 1. Clone the Repository

```bash
git clone https://github.com/Mash-ruela/late-show-api-challenge.git
cd late-show-api-challenge/server

### 2. Install Dependencies
```bash
pipenv install
pipenv shell

### 3. Create .env File
In the server/ directory:
env
DATABASE_URI=postgresql://your_user:your_password@localhost:5432/late_show_db
JWT_SECRET_KEY=supersecretkey

Make sure the database late_show_db exists in PostgreSQL:
```bash
createdb late_show_db

###  4. Initialize the Database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

### 5. Seed the Database
```bash
flask run

Server running at: http://127.0.0.1:5000

### Authentication Flow

Register
POST /register

json
{
  "username": "admin",
  "password": "admin123"
}

Login
POST /login

json
{
  "username": "admin",
  "password": "admin123"
}
Response:

json
{
  "token": "your_jwt_token"
}

Route List
Method	Endpoint	Description	Auth Required
POST	/register	Register a new user	
POST	/login	Login and get JWT token
GET	/guests	Get all guests	
GET	/episodes	Get all episodes	
GET	/episodes/<id>	Get specific episode	
DELETE	/episodes/<id>	Delete an episode	
POST	/appearances	Create a new appearance	


Postman Usage
Import the provided Late Show API.postman_collection.json into Postman.

Use the Register and Login requests first.

Copy the JWT token from Login response and use it in Authorization headers as:

php-template
Bearer <your_token>
Use protected routes like /appearances and /episodes/:id (DELETE) with the token.

REPO
https://github.com/Mash-ruela/late-show-api-challenge.git

 Live API Base URL
http://127.0.0.1:5000


