#!/bin/bash
echo "Setting up the project..."

# Install uv if not found
if ! command -v uv &> /dev/null
then
    echo "uv not found, installing via pip..."
    pip install uv
fi

# Sync dependencies
uv sync

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating default .env file..."
    echo "SECRET_KEY=django-insecure-development-key" > .env
    echo "DEBUG=True" >> .env
    echo "ALLOWED_HOSTS=127.0.0.1,localhost" >> .env
fi

# Run migrations
uv run python manage.py migrate

echo "Setup complete!"
