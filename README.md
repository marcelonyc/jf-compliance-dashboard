# JFrog Compliance Dashboard
This project provides a scheduler to regularly download data from JFrog and Dashboards using Apache Superset to visualize.

## Available Data
- Artifact Repositories
- Watches
- Policies
- Violations

## Simple setup

1. Clone this repo
2. Make a copy of docker/.env as docker/.env-local (this file is included in .gitignore)
3. Add values for JF_URL and JF_TOKEN 
4. From the root directory run
    a. docker compose up

* The initial start takes a few minutes. Give it 10 minutes on the first `up` before you continue
* Loading the data runs on a schedule. It might take a few minutes to complete the load



