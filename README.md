# CoreStock V1

CoreStock is a full-stack inventory and warehouse management application inspired by real ERP and WMS workflows.

The project was built to explore practical stock management concepts such as products, warehouses, inventory quantities, stock movements, low-stock monitoring, and demo environment management.

## Live Demo

**Application:** https://corestock-v1.vercel.app

The application is publicly deployed and includes a resettable demo environment, allowing inventory workflows to be tested from a clean and consistent state.

## Features

* Product catalog management
* Warehouse and location management
* Inventory tracking across locations
* Purchase, sale, and transfer stock movements
* Low-stock monitoring
* Dashboard with inventory statistics
* Resettable demo environment

## Tech Stack

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic
* PostgreSQL
* Pytest

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Deployment

* Vercel (Frontend)
* Railway (Backend)
* Supabase (PostgreSQL Database)

## Architecture

CoreStock follows a modern full-stack architecture:

```text
Next.js Frontend
        ↓
FastAPI REST API
        ↓
PostgreSQL Database
```

The frontend consumes REST endpoints exposed by the FastAPI backend, while SQLAlchemy handles data access and Alembic manages database migrations.

## Screenshot

### Dashboard

![CoreStock Dashboard](public/projects/corestock/dashboard.png)

## Purpose

This project was created to demonstrate practical full-stack development skills through a realistic inventory management workflow inspired by ERP and warehouse management systems.
