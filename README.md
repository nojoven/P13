# P13
Projet final D.A. Python Openclassrooms


# Create the application's project

Open your terminal and run:
- "django-admin.py startproject weatwork ."
Where '.' is the *WORKDIR* that is defined in our dockerfile. 

# Run the application

# Generate the secret key

Use this command in your terminal:
- *python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'*

The command is :
- docker-compose run weatwork

# Run unit _tests

The command is :
docker-compose run weatwork sh -c "python manage.py test"

# Apply database migrations on a specific Django app

The command is :
docker-compose run weatwork sh -c "python manage.py makemigrations <*YOUR_APP_NAME*>"

