# JFrog Compliance Dashboard
This project provides a scheduler to regularly download data from JFrog and Dashboards using Apache Superset to visualize.

Table of Content

- [Available Data](#available-data)
- [Setup](#setup)
    - [All-in-One setup](#all-in-one-setup)
    - [Data Loader Only](#dataloader-only)
- [Import Dashboards](#import-dashboards)
- [Login to Superset](#login-to-superset)
- [Other endpoints](#other-endpoints)
    - [Job Queue](#job-queue)

## Available Data
- Artifact Repositories
- Watches
- Policies
- Violations
- Licenses

## Setup

### All in One Setup
This setup includes the data loader and a version of Superset

1. Clone this repo
2. Make a copy of docker/.env as docker/.env-local (this file is included in .gitignore)
    - The file must be in the same location as .env-jfrog and exact name.
3. Add values for JF_URL and JF_TOKEN 
4. From the root directory run `docker compose up`

* The initial start takes a few minutes. Give it 10-20 minutes on the first `up`
* Wait until you see `dashbosard-app` displaying output on the logs before you continue
* In some instances, Superset did not come up correctly. run `docker compose stop` and `docker compose up` to restart.
* Loading the data runs on a schedule. It might take a few minutes to complete the load


### Dataloader only 

>WORK IN PROGRESS: FOLLOW THE ALL-IN_ONE SETUP AND SKIP TO [Import Dashboards](#import-dashboards)

This setup does not iclude Superset. It exposes the Postgres db port to the localhost.

1. Clone this repo
2. Make a copy of docker/.env-jfrog as docker/.env-local-jfrog (this file is included in .gitignore)
    - The file must be in the same location as .env-jfrog and exact name.
3. Add values for JF_URL and JF_TOKEN 
4. From the root directory run `docker compose -f e -f  docker-dataloader-only.yaml --project-name jfrog-dashboard up`
    - We add `project-name` to create a docker network we can share with a Superset deployment
5. Clone Superset (https://github.com/apache/superset.git)
    - Do not clone under the root of the data loader
6. Start Superset 
    - (Optional) Make a copy of docker/.env as docker/.env-local (this file is included in .gitignore)
    - `docker compose e -f  docker-compose-non-dev.yml --project-name jfrog-dashboard up`

## Import Dashboards

From the root directory of this project run 

`# ./import-dashboards.sh`

## Login to Superset
Once the environment is up go to http://localhost:8088

Default credentials
- user: admin
- pass: admin


For more information on Apache Superset, visit [Superset](https://superset.apache.org).

## Other endpoints

### Job Queue
Monitor the execution of the data loading jobs
https://loalhost:9181