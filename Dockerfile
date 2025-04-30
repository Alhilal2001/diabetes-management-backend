# Dockerfile للـ Django Backend

# Use official python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy project
COPY . /app/

# Run server
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
