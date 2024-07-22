# TweetLake

Welcome to TweetLake! This Django project allows users to create accounts, log in, post tweets, view tweets, and search for tweets. The project uses Django's inbuilt UserCreationForm for user registration and provides robust user authentication features.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **User Registration**: Users can create accounts using Django's inbuilt UserCreationForm.
- **User Authentication**: Secure user login and logout functionality.
- **Post Tweets**: Logged-in users can post tweets.
- **View Tweets**: Users can view all tweets.
- **Search Tweets**: Users can search for specific tweets using keywords.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- Virtualenv (optional but recommended)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/RutwikGaikwad/TweetLake.git
   cd TweetLake
2. **Create a virtual environment and activate it (optional but recommended)**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt

4. **Apply migrations to set up the database**:

   ```bash
   python manage.py migrate

5. **Create a superuser (optional, for accessing the admin site)**:

   ```bash
   python manage.py createsuperuser

6. **Run the development server**:

   ```bash
   python manage.py runserver
7. **Open your web browser and navigate to http://127.0.0.1:8000 to access the application.**

## Usage
- **User Registration and Login**
  1. Navigate to the registration page (/register/) to create a new account.
  2. After registration, log in to your account at the login page (/login/).
- **User Authentication**
  1. Login: Use your credentials to log in at /login/.
  2. Logout: You can log out by clicking the logout button or navigating to /logout/.
 - **Posting Tweets**
   1. Once logged in, click on the New Tweet button to post a new tweet.
   2. Fill in the tweet content and submit.
  - **Viewing and Searching Tweets**
    1. To view all tweets, go to the homepage (/).
    2. Use the search bar on the homepage to search for specific tweets using keywords.
