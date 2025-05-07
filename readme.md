---
title: "Template App Django"
author: "Ribera Andres"
date: "1/01/2023"
output: html_document
---

# Django + Tailwind Template 🚀 
This project is built using the Django framework for backend development, providing a robust architecture based on the MTV (Model-Template-View) pattern, with a powerful ORM system and built-in administrative tools. For the frontend, Tailwind CSS is used, a utility-first CSS framework that enables rapid and precise construction of responsive user interfaces, maintaining a clean and consistent design. The development and deployment environment is fully containerized using Docker, ensuring portability, reproducibility, and dependency isolation across environments. This tech stack enables efficient integration between server-side logic, modern visual design, and infrastructure operations.

[![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)


## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/andresriberae/nest-pokedex.git
   cd nest-pokedex
   ```

2. **Initialize Development Environment**
    ```bash
        # First, initialize development tools and commands
        source bin/setup

        # Then, configure your development environment
        configure
    ```

    ```bash
        # Install environment in windows
        python -m venv venv


        # Active environment
        .\venv\Scripts\activate
    ```

    > Once activated, your terminal should display the **(env)** prefix.

3. **Install Required Libraries** 📦 

    ```bash
        # Install Django
        pip install django
    ```

    Install all dependencies listed in the requirements file:
    ```bash
        pip install -r requirements.txt
    ```

4. **Run Migrations** 🛠️
    Apply initial migrations:

    ```bash
    python manage.py migrate
    ```


5. **Run the Development Server**🧪

    ```bash
    python manage.py runserver
    ```

    Run Tailwind:

    ```bash
    python manage.py tailwind start
    ```

---

#  8. Run Docker 🐳

Build the Docker image

```bash
docker build -t devrrior/docker-django .
```

Run the container on port 8000

```bash
docker run -p 8000:8000 devrrior/docker-django
```

Run with volume to enable real-time changes

```bash
docker run -v /Users/hp/Desktop/DjangoProject/django_crud/:/app -p 8000:8000 devrrior/docker-django
```

Run in detached mode (background)

```bash
docker run -d -v /Users/hp/Desktop/DjangoProject/django_crud/:/app -p 8000:8000 devrrior/docker-django
```

View container logs

```bash
docker logs --follow <id_del_contendor>
```

Stop the container

```bash
docker stop devrrior/docker-django
```

Access the container shell

```bash
docker exec -it <id_del_contendor> /bin/sh
```

> For further help, refer to the [documentación oficial de Django](https://docs.djangoproject.com/es/4.0/).