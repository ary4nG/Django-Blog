# Django Blog Project

A modern, feature-rich blog platform built with Django and PostgreSQL. This project supports categories, tags, comments, and a powerful admin dashboard. It is ready for local development and Docker deployment.

---

## Features

- **Homepage:** Paginated list of latest published posts.
- **Post Detail:** Full post content, author, category, tags, comments, and related posts.
- **Categories & Tags:** Browse posts by category or tag.
- **Comments:** Users can comment on posts (admin approval required).
- **Admin Dashboard:** Manage posts, categories, tags, and comments with custom admin features.
- **Pagination:** Easy navigation for long lists of posts.
- **Responsive Design:** Uses Bootstrap for a clean, mobile-friendly layout.
- **Docker Support:** Easy setup for local development with PostgreSQL.

---

## Tech Stack

- **Backend:** Django 5.2.1 (Python)
- **Database:** PostgreSQL (via Docker)
- **Frontend:** HTML, Bootstrap (templates)
- **Environment:** `.env` for secrets and config
- **Containerization:** Docker & Docker Compose

---

## Getting Started

### Prerequisites

- Python 3.13+
- pip
- Docker & Docker Compose (recommended)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root with your settings:
     ```
     SECRET_KEY=your-secret-key
     DEBUG=True
     DB_NAME=blog_db
     DB_USER=blog_user
     DB_PASSWORD=your-db-password
     DB_HOST=localhost
     DB_PORT=5432
     ALLOWED_HOSTS=localhost,127.0.0.1
     ```

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the site:**
   - Blog: [http://localhost:8000/](http://localhost:8000/)
   - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

### Using Docker

1. **Copy your `.env` file to the project root.**

2. **Build and start containers:**
   ```bash
   docker-compose up --build
   ```

3. **Run migrations inside the container:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create a superuser:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

---

## Custom Admin Features

- **Category & Tag:** Search, filter, and auto-generate slugs.
- **Post:** Only superusers see all posts; regular users see their own. Author auto-assigned on creation.
- **Comment:** Bulk approve/disapprove actions.

---

## Environment Variables

Set these in your `.env` file:

- `SECRET_KEY`: Django secret key
- `DEBUG`: `True` for development, `False` for production
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`: PostgreSQL settings
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

---

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [PostgreSQL](https://www.postgresql.org/)

---

