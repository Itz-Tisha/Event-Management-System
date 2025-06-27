# 🎉 Event Management System

A web-based Event Management System built using Django, designed to help clubs manage events, users register for events, and collect feedback efficiently. It supports organizers and participants, club creation, event scheduling, and user registration.

## 🛠️ Tech Stack

- Framework:Django (Python)
- Frontend:HTML, CSS, Bootstrap 
- Database:SQLite3 
- Media Storage: Django's `ImageField` for profile, club, and event images

## 📌 Key Features

### 👤 User Management
- Two types of users: `Organizer` and `Participant`
- Profile images for users
- Secure registration and login

### 🏢 Club Management
- Organizers can create clubs
- Each club has its own description and logo

### 📅 Event Management
- Clubs can create and manage events
- Event images, description, location, date, and time
- Attendee count tracking

### 📝 Event Registration
- Participants can register for events
- Registration records stored with name, email, and event

### 💬 Feedback System
- Users can submit feedback for events

## 📂 Models Overview

### `UserType`
Represents the users of the system.
- Fields: `name`, `email`, `password`, `user_type (organizer/participant)`, `profile_image`

### `club`
Represents a club managed by an organizer.
- Fields: `clubname`, `desc`, `org_name (FK to UserType)`, `image`

### `event`
Stores individual event data.
- Fields: `event_name`, `location`, `start_time`, `end_time`, `date`, `desc`, `club_name (FK)`, `attendee`, `image`

### `event_reg`
Stores registrations for each event.
- Fields: `name`, `email`, `event_name (FK)`

### `feedback`
Stores feedback for events.
- Fields: `name`, `feedback`, `event_name (FK)`
