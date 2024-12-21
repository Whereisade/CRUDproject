# CRUDProject

CRUDProject is a Django REST Framework application that implements CRUD (Create, Read, Update, Delete) operations for managing `Books` and `Authors`. It includes APIs to add, retrieve, update, and delete entries.

## Project Setup

### Requirements
- Python 3.8+
- Django 4.0+
- Django REST Framework

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CRUDProject
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv virtualenv
   virtualenv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the server:
   ```
   python manage.py runserver
   ```

6. Access the application at:
   ```
   http://127.0.0.1:8000/
   ```

## API Endpoints

### AppOne (Books Management)

#### 1. **List all books**
- **URL**: `/api/appone/books/`
- **Method**: `GET`
- **Response Example**:
  ```json
  [
    {
      "id": 1,
      "title": "Django for Beginners",
      "author": "William S. Vincent",
      "publication_date": "2023-01-15"
    },
    {
      "id": 2,
      "title": "Two Scoops of Django",
      "author": "Daniel Roy Greenfeld",
      "publication_date": "2023-05-20"
    }
  ]
  ```

#### 2. **Retrieve a specific book**
- **URL**: `/api/appone/books/<id>/`
- **Method**: `GET`
- **Response Example**:
  ```json
  {
    "id": 1,
    "title": "Django for Beginners",
    "author": "William S. Vincent",
    "publication_date": "2023-01-15"
  }
  ```

#### 3. **Create a new book**
- **URL**: `/api/appone/books/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "title": "Django Rest Framework Guide",
    "author": "John Doe",
    "publication_date": "2024-01-01"
  }
  ```
- **Response Example**:
  ```json
  {
    "id": 3,
    "title": "Django Rest Framework Guide",
    "author": "John Doe",
    "publication_date": "2024-01-01"
  }
  ```

#### 4. **Update a book**
- **URL**: `/api/appone/books/<id>/`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "title": "Updated Book Title",
    "author": "Updated Author",
    "publication_date": "2024-02-01"
  }
  ```
- **Response Example**:
  ```json
  {
    "id": 3,
    "title": "Updated Book Title",
    "author": "Updated Author",
    "publication_date": "2024-02-01"
  }
  ```

#### 5. **Delete a book**
- **URL**: `/api/appone/books/<id>/`
- **Method**: `DELETE`
- **Response**: `204 No Content`

---

### AppTwo (Authors Management)

#### 1. **List all authors**
- **URL**: `/api/apptwo/authors/`
- **Method**: `GET`
- **Response Example**:
  ```json
  [
    {
      "id": 1,
      "name": "J.K. Rowling",
      "bio": "British author, best known for the Harry Potter series.",
      "date_of_birth": "1965-07-31"
    },
    {
      "id": 2,
      "name": "George R.R. Martin",
      "bio": "American novelist, author of A Song of Ice and Fire.",
      "date_of_birth": "1948-09-20"
    }
  ]
  ```

#### 2. **Retrieve a specific author**
- **URL**: `/api/apptwo/authors/<id>/`
- **Method**: `GET`
- **Response Example**:
  ```json
  {
    "id": 1,
    "name": "J.K. Rowling",
    "bio": "British author, best known for the Harry Potter series.",
    "date_of_birth": "1965-07-31"
  }
  ```

#### 3. **Create a new author**
- **URL**: `/api/apptwo/authors/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "Isaac Asimov",
    "bio": "American author and professor of biochemistry, famous for his works of science fiction.",
    "date_of_birth": "1920-01-02"
  }
  ```
- **Response Example**:
  ```json
  {
    "id": 3,
    "name": "Isaac Asimov",
    "bio": "American author and professor of biochemistry, famous for his works of science fiction.",
    "date_of_birth": "1920-01-02"
  }
  ```

#### 4. **Update an author**
- **URL**: `/api/apptwo/authors/<id>/`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "name": "Updated Author Name",
    "bio": "Updated biography.",
    "date_of_birth": "1921-01-03"
  }
  ```
- **Response Example**:
  ```json
  {
    "id": 3,
    "name": "Updated Author Name",
    "bio": "Updated biography.",
    "date_of_birth": "1921-01-03"
  }
  ```

#### 5. **Delete an author**
- **URL**: `/api/apptwo/authors/<id>/`
- **Method**: `DELETE`
- **Response**: `204 No Content`

---
- Tested the APIs using Postman

---


