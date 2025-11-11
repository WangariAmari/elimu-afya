FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install minimal build deps for some Python packages (remove lists to save space)
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential libpq-dev gcc \
 && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Use python -m pip and --no-cache-dir
RUN python -m pip install --upgrade pip setuptools wheel \
 && python -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Create non-root user and set ownership
RUN addgroup --system django && adduser --system --ingroup django django \
 && chown -R django:django /app

USER django

EXPOSE 8000

# For development: run migrations then runserver
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
