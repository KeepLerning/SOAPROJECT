FROM python:3.13

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

COPY start.sh /start.sh
RUN sed -i 's/\r$//' /start.sh && chmod +x /start.sh

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install project dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "-c", "/start.sh"]