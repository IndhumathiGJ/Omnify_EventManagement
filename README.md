
# Event Management API

This Django REST API allows you to create and list events, register attendees, and view attendees for specific events.

## Features

- Create an event
- List all events
- Register an attendee for an event
- View attendees of a specific event
- Swagger UI for API documentation

## Setup Instructions

### 1. Clone the repository or unzip the folder

```
git clone 
cd event-management
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

## API Endpoints

| Method | Endpoint                                  | Description                            |
|--------|-------------------------------------------|----------------------------------------|
| POST   | `/api/createevent`                        | Create a new event                     |
| GET    | `/api/events/`                            | List all events                        |
| POST   | `/api/events/<event_id>/register`         | Register attendee for a specific event|
| GET    | `/api/events/<event_id>/attendees`        | List attendees for a specific event    |
| GET    | `/swagger/`                               | Swagger UI for API documentation       |

## Assumptions

- SQLite is used for simplicity.
- Each event has a name, location, date, and time.
- Attendees are identified by name and email.

## Sample API Requests

### Create an Event

**POST** `/api/createevent`

```json
{
    "name": "Tech Summit 2025",
    "location": "Chennai",
    "date": "2025-08-01",
    "time": "10:00:00"
}
```

### Register an Attendee

**POST** `/api/events/1/register`

```json
{
    "name": "John Doe",
    "email": "john@example.com"
}
```

### View Attendees

**GET** `/api/events/1/attendees`



## Video Walkthrough

A Loom video walkthrough link will be shared separately.

---
