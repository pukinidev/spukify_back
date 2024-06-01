# Spukify Backend Project

## How to run the project?
### Local
- First install dependencies and then in VSCODE just press play buttom. You need to change the database settings and use SQLITE, POSTGRESQL or another one of that you like.
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





