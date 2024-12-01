#! /bin/bash


# Database migrations
alembic upgrade head 

cd /app/src

# Start job queue workers
# 3 parallel workers
rq worker --with-scheduler -u redis://redis:6379/1 &
rq worker --with-scheduler -u redis://redis:6379/1 &
rq worker --with-scheduler -u redis://redis:6379/1 &

rqscheduler --host redis --port 6379 --db 1 &

rq-dashboard -u redis://redis:6379/1 &



python dataloading.py

