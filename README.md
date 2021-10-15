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


# Recommended links:


- https://docs.docker.com/engine/reference/builder/

- https://docs.docker.com/compose/

- https://docs.docker.com/compose/reference/run/

- https://docs.djangoproject.com/en/3.2/topics/auth/customizing/

- https://docs.djangoproject.com/en/3.2/topics/auth/customizing/

- https://docs.djangoproject.com/en/3.2/topics/auth/customizing/

- https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager.normalize_email

- https://docs.djangoproject.com/en/3.2/ref/django-admin/

- https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

- https://docs.djangoproject.com/en/3.2/ref/contrib/admin/



- https://docs.travis-ci.com/user/tutorial/

-https://docs.travis-ci.com/user/job-lifecycle/#customizing-the-build-phase

- https://flake8.pycqa.org/en/latest/

- https://docs.djangoproject.com/en/3.2/internals/contributing/writing-code/unit-tests/

- https://docs.python.org/3/library/unittest.html#assert-methods

- https://github.com/dadarek/docker-wait-for-dependencies

- https://stackoverflow.com/questions/52621819/django-unit-test-wait-for-database

- https://docs.djangoproject.com/en/3.2/ref/django-admin/#django.core.management.call_command

- https://github.com/django/django/blob/11b8c30b9e02ef6ecb996ad3280979dfeab700fa/django/db/utils.py#L195
