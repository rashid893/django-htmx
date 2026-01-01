# Use official Python slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies directly
RUN pip install --upgrade pip \
    && pip install django \
    django-crispy-forms \
    crispy-bootstrap5 \
    django-forms-bootstrap \
    htmx

# Copy project files
COPY . .

# Optional: collect static files if using Tailwind build
# RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

