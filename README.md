# The Monolith

**The Monolith** is a full-stack digital art gallery platform built for curators and art enthusiasts to explore, filter, and interact with curated collections of artwork.

---

## Features
- **Curated Exhibition Home:** Browse artwork collections with dynamic category tag filtering.
- **Artwork Details & Interactions:** Inspect single pieces and like/unlike artwork dynamically.
- **Curator Accounts & Authentication:** Secure email registration, login, and **Google OAuth** integration via `django-allauth`.
- **Profile Management:** Clean view-only profiles and custom edit views supporting avatar updates via **Cloudinary**.
- **Password Reset Flow:** Fully styled password recovery workflow matching the project's earth-tone theme.
- **Production Ready:** Configured with **PostgreSQL**, **WhiteNoise** for static assets, and `django-crispy-forms` (Bootstrap 5).

---

## Tech Stack
* **Backend:** Python, Django 6.1
* **Database:** SQLite (Local) / PostgreSQL (Production)
* **Media Storage:** Cloudinary
* **Frontend:** HTML5, Tailwind CSS / Crispy Forms
* **Deployment:** Render

---

## Local Development & Setup Guide

Follow these steps carefully to get the project running on your local machine:

### 1. Clone the repository
Open your terminal and clone the project repository from GitHub, then navigate into the project directory:
```bash
git clone https://github.com/lameckkipsang/the_monolith.git
cd the-monolith
```

### 2. Create and activate a virtual environment
Set up an isolated Python environment to manage project dependencies:
```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows (Command Prompt / PowerShell):
venv\Scripts\activate

# On macOS / Linux:
source venv/bin/activate
```

### 3. Install dependencies
Install all required Python packages (including Django, Cloudinary, WhiteNoise, and Crispy Forms) listed in the requirements file:
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the root directory of your project and populate it with your local configuration keys:
```env
SECRET_KEY=your_django_secret_key_here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

### 5. Apply database migrations
Set up your database tables by running Django's migration command:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser account
To access the Django Admin panel and manage artworks and categories, create an administrative user account:
```bash
python manage.py createsuperuser
```
*(Follow the prompts to enter your username, email, and password).*

### 7. Run the development server
Start the local development server:
```bash
python manage.py runserver
```

### 8. Access the application
Open your web browser and navigate to:
- **Main Gallery App:** http://127.0.0.1:8000/
- **Admin Dashboard:** http://127.0.0.1:8000/admin/ *(log in using the superuser credentials you created in Step 6).*

---

## License
This project is open-source and available under the [MIT License](LICENSE).