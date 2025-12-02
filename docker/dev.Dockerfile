FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install OS-level dependencies needed for mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    libmariadb-dev-compat \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements/base.txt /app/requirements/base.txt
COPY requirements/dev.txt /app/requirements/dev.txt

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt

# Copy the actual project
COPY . /app

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
