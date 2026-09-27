#!/usr/bin/env bash
set -e

# Wait for Postgres
host_port="${DATABASE_HOST:-db}:${DATABASE_PORT:-5432}"

echo "Waiting for database at $host_port..."

# simple loop to wait
until nc -z ${DATABASE_HOST:-db} ${DATABASE_PORT:-5432}; do
  echo "Waiting for Postgres..."
  sleep 1
done

# Run migrations (if alembic present)
if [ -f alembic.ini ]; then
  echo "Running alembic upgrade head"
  alembic upgrade head || true
fi

# Start web server
uvicorn main:app --host 0.0.0.0 --port 8000
