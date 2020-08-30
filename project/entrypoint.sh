#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z web-db 5432; do
  sleep 0.1
done

echo "PostreSQL started"
# note for Windows users - use git bash to run dos2unix.exe entrypoint.sh to fix file format issue
exec "$@"
