#!/bin/sh
echo "Checking if the postgres database is ready..."

until pg_isready -h postgres -p 5432; do
  echo "Database is not ready yet, trying again in 3 seconds..."
  sleep 3
done

echo "The database is ready!"