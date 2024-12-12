# time-management
Basic python project using django
Task Manager - Django Application

This is a Django-based Task Manager application that allows you to create, update, view, and delete tasks via the Django admin panel.

Prerequisites

Before setting up the project, ensure you have the following installed:

Python 3.12 or higher

Django 5.1.4

SQLite (default database for Django)

Setup Instructions

1. Clone the Repository

If you are starting from scratch, create a new Django project and app. Otherwise, clone the project repository:
# Clone the repository (if applicable)
git clone <repository_url>
cd task_manager

2. Create a Virtual Environment

Set up a virtual environment to isolate dependencies:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

Install Django and any other dependencies:

pip install -r requirements.txt

Apply migrations

python3 manage.py makemigrations
python3 manage.py migrate


8. Create a Superuser

Create an admin user to manage tasks:

python3 manage.py createsuperuser

Provide the required details such as username, email, and password.

Run the Development Server
python3 manage.py runserver

Access the application at:

http://127.0.0.1:8000/

Using the Application

Access the Admin Panel:

Visit http://127.0.0.1:8000/admin/.

Log in using the superuser credentials.

Manage Tasks:

Add, update, and delete tasks directly through the admin panel.

Contact

For any queries, feel free to reach out at:

Name: Santosh Vana

Email: vanasanthosh545@gmail.com>
