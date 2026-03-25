# PropertyNest Real Estate Platform

PropertyNest is a Django-powered demo platform that showcases modern real estate product workflows in a single dashboard UI. It is designed as a realistic front-end and product prototype for buyers/tenants, agents, property owners, and admins.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Available Route](#available-route)
- [Configuration Notes](#configuration-notes)
- [Testing](#testing)
- [Future Improvements](#future-improvements)

## Overview

The application serves a single, rich dashboard page that combines:

- property discovery and filtering,
- favorites and shortlist management,
- mortgage estimation,
- visit scheduling,
- document status tracking,
- agent reputation signals,
- neighborhood analytics.

The backend provides curated seed data through Django templates and JSON payloads, while the frontend handles interactive filtering, rendering, and user-driven calculations.

## Key Features

### 1) Multi-role platform presentation
- Highlights support for **Buyer / Tenant**, **Agent**, **Property Owner**, and **Admin** personas.
- Displays role pills in the hero area to frame stakeholder coverage.

### 2) Listings catalog with rich metadata
- Ships with multiple pre-seeded listings across different cities.
- Each listing includes:
  - title and location,
  - property type,
  - buy/rent intent,
  - price,
  - beds/baths/area,
  - assigned agent,
  - agent rating,
  - image,
  - description,
  - feature tags.

### 3) Advanced filtering controls
- Filter by:
  - location,
  - property type,
  - intent (buy/rent),
  - max price (range slider),
  - favorites-only toggle.
- Real-time filtering updates listing cards and result counts.
- Includes reset behavior to restore defaults.

### 4) Dynamic listing rendering
- Listings are rendered on the client from JSON seed data.
- Listing cards include:
  - responsive image,
  - floor-plan badge,
  - formatted price (including `/mo` for rentals),
  - descriptive metadata,
  - tag chips,
  - agent summary,
  - favorite toggle button.

### 5) Favorites + shortlist workflow
- Users can favorite/unfavorite listings via heart action.
- Favorites are tracked in in-memory state and reflected immediately in UI.
- Shortlist panel displays all selected properties.
- Empty-state guidance appears when no favorites are selected.

### 6) Mortgage calculator
- Interactive monthly payment estimate using:
  - home price,
  - down payment percentage,
  - interest rate,
  - term length in years.
- Displays monthly principal/interest estimate and loan amount breakdown.

### 7) Visit scheduling form
- Users can select a property, date, and time.
- Submitting the form shows a confirmation message for the selected listing.

### 8) Document management panel
- Shows role-linked transaction documents.
- Status chips support:
  - approved,
  - pending,
  - missing.

### 9) Agent reviews and trust signals
- Displays a curated set of agent reviews and star ratings.
- Helps model trust-building UX for conversion-oriented real estate flows.

### 10) Neighborhood analytics
- Presents area-level intelligence including:
  - walk score,
  - schools grade,
  - YoY growth,
  - average days on market (DOM).

### 11) Responsive UI and modern visual design
- CSS-driven card layout, gradients, chips, sticky sidebar behavior, and responsive breakpoints.
- Adaptive structure for desktop/tablet/mobile widths.

## Tech Stack

- **Backend:** Django 4.2+ (compatible with < 5.2)
- **Frontend:** Server-rendered HTML + vanilla JavaScript + CSS
- **Data Store:** SQLite (default Django development database)
- **Static Assets:** Django staticfiles (`/static/listings/...`)

## Project Structure

```text
PropertyNest-Real-Estate-Platform/
├── listings/
│   ├── apps.py
│   ├── tests.py
│   └── views.py                # Dashboard view + seed data
├── propertynest/
│   ├── settings.py             # Django config
│   ├── urls.py                 # URL routing
│   ├── asgi.py
│   └── wsgi.py
├── static/
│   └── listings/
│       ├── app.js              # UI interactivity and state handling
│       └── styles.css          # Platform styling + responsiveness
├── templates/
│   └── listings/
│       └── dashboard.html      # Main dashboard template
├── manage.py
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.10+ recommended
- pip

### 1) Clone the repository

```bash
git clone <your-repo-url>
cd PropertyNest-Real-Estate-Platform
```

### 2) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run migrations

```bash
python manage.py migrate
```

### 5) Start the development server

```bash
python manage.py runserver
```

### 6) Open in your browser

Visit:

```text
http://127.0.0.1:8000/
```

## How It Works

1. Django route `/` maps to the `dashboard` view.
2. The view builds context from in-memory seed datasets (listings, documents, reviews, analytics).
3. Template renders static page structure and embeds `seed_data_json` via Django `json_script`.
4. Frontend script reads seed data and controls interactive behavior:
   - listing filtering,
   - favorites state updates,
   - shortlist rendering,
   - mortgage calculation,
   - visit form confirmation.

## Available Route

- `/` → Main PropertyNest dashboard
- `/admin/` → Default Django admin route

## Configuration Notes

- `DEBUG = True` and `ALLOWED_HOSTS = ['*']` are set for demo/development convenience.
- The secret key in this repository is development-only and should be replaced for production.
- SQLite is used by default and stored at `db.sqlite3`.

## Testing

Run default Django tests:

```bash
python manage.py test
```

> Note: The current test module is a scaffold and can be expanded with unit and integration coverage.

## Future Improvements

- Add persistent database models for listings, leads, tours, and documents.
- Add authentication and role-based access control.
- Add backend APIs (DRF/GraphQL) for live data.
- Add map integration and geospatial search.
- Add saved searches and notification workflows.
- Add CI checks and richer automated test coverage.
- Harden production settings and deployment configuration.

---

If you want, I can also generate:
- a production-ready README variant (deploy-focused),
- API documentation scaffolding,
- contribution guidelines (`CONTRIBUTING.md`),
- and issue/PR templates.
