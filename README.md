# 🌿 Vanvrindha

A premium botanical e-commerce platform built using Django and MySQL, designed to provide a luxury plant-shopping experience while demonstrating enterprise-level software architecture principles such as Repository Pattern and Service Layer Architecture.

---

# Project Overview

Vanvrindha is a full-stack web application that allows users to browse plants, search products, manage carts, place orders, and interact with a visually rich botanical marketplace.

The project was developed with a focus on:

* Clean architecture
* Scalable code organization
* Separation of concerns
* Database-driven development
* User authentication and authorization
* Admin product management

Unlike traditional Django CRUD projects, Vanvrindha follows a layered architecture using Repository and Service patterns to simulate real-world software development practices.

---

# Architecture

The application follows a layered architecture:

User Interface (Templates)
↓
Views Layer
↓
Service Layer
↓
Repository Layer
↓
MySQL Database

### Layers

#### 1. Views Layer

Handles HTTP requests and responses.

Responsibilities:

* Route handling
* Request validation
* Rendering templates
* Redirects

#### 2. Service Layer

Contains business logic.

Responsibilities:

* User authentication
* Product operations
* Order processing
* Category handling

#### 3. Repository Layer

Handles database interaction.

Responsibilities:

* Data retrieval
* Data persistence
* Query execution

#### 4. Database Layer

Stores application data in MySQL.

# Features

### User Features

* User Registration
* User Login
* Logout Functionality
* Product Browsing
* Product Details View
* Product Search
* Category Filtering
* Shopping Cart
* Checkout Process
* Order Placement

### Admin Features

* Product Creation
* Product Editing
* Product Deletion
* Order Management
* Inventory Monitoring
* Protected Admin Access

### UI Features

* Luxury Botanical Theme
* Responsive Layout
* Background Video Integration
* Glassmorphism Components
* Custom Branding

---

# Tech Stack

### Backend

* Python
* Django

### Database

* MySQL

### Frontend

* HTML5
* CSS3
* JavaScript

### Development Tools

* VS Code
* Git
* GitHub

### Design Concepts

* Repository Pattern
* Service Layer Architecture
* MVC-inspired Structure

---

# Database Design

### Main Tables

#### auth_user

Stores Django user accounts.

#### user_profile

Stores extended user information.

#### category

Stores plant categories.

#### product

Stores product details.

#### orders

Stores customer orders.

#### order_items

Stores individual order items.

#### django_session

Manages active sessions.

---

# Project Structure

```text
myweb/
│
├── master/
│   ├── Entity/
│   ├── Repository/
│   ├── services/
│   ├── views.py
│   └── models.py
│
├── static/
│   ├── css/
│   ├── images/
│   └── videos/
│
├── templates/
│   ├── admin/
│   └── user pages
│
├── myweb/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---

# Installation

### Clone Repository

```bash
git clone https://github.com/vaikunthprajapati/Vanvrindha.git
```

### Move Into Project

```bash
cd Vanvrindha
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Create a MySQL database:

```sql
CREATE DATABASE vanvrindha;
```

Update database settings inside:

```text
myweb/settings.py
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

# Learning Outcomes

This project helped me gain practical experience with:

* Django Web Development
* MySQL Integration
* Authentication Systems
* Session Management
* Repository Pattern
* Service Layer Architecture
* MVC Concepts
* Frontend Styling
* Git & GitHub Workflow

---

# Future Enhancements

Planned improvements include:

* REST API Development
* JWT Authentication
* Docker Deployment
* React Frontend Integration
* Cloud Media Storage
* Inventory Management System
* Recommendation Engine
* Advanced Analytics Dashboard

---

# Author

**Vaikunth Prajapati**

GitHub:
https://github.com/vaikunthprajapati

---

# License

This repository is provided for educational and evaluation purposes.

Viewing is permitted.

Reuse, redistribution, modification, or commercial usage without permission is prohibited.
