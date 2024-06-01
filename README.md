# Spukify Backend Project

## About the project

### Author

Valeria Caro 

### Description

TO-DO: Add a brief description

## How to run the project?
### Local
- First install dependencies and then in Visual Studio Code just press play buttom. You need to change the database settings and use SQLITE, POSTGRESQL or another one that you like. Highly recommended the use of a python virtual environment!
```python
pip3 install -r requirements.txt
```

### Docker

- Docker is required, so first download it from their official page (https://www.docker.com/products/docker-desktop/). Inside the project folder you find the Dockerfile and the docker-compose.yml that is alredy configured with a POSTGRESQL database and a python container to run the fastapi app. In the root of project, run the next command to deploy the containers in docker.

```docker
docker-compose up -d
```

- To stop and remove the containers use

```docker
docker-compose down
```
## Populate the database

The project also includes a file that generate data to fill the database. This file you can find it inside the data folder. It is needed a .env file to store you Spotify Credentials because the python library "Spotipy" needs to gather the information from spotify using those credentials. Also there are json files with data to fill the database if you need it on "/data/data_json/".

- Remember to install spotipy using the next comand

    ```python
    pip3 install spotipy
    ```
- Then you can run the spotifyinfo.py file to generate the data!




