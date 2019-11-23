# Docker builder

Simple builder tool which will download repository from Github, build a dockerfile from repository root and publish the built image to Docker Hub.

## Building the builder

Pull the builder tool from Docker Hub:

```
docker pull tomirantanen/docker-builder
```

Or build from dockerfile:

```
docker build -t docker-builder .
```

## Running

### Environment variables

Dockerhub credentials are needed for pushing the images.
Provide credentials as env file or from command line.

Example env:

```
DOCKER_USERNAME=username
DOCKER_PASSWORD=password

```

### Command line parameters

| Name | Description        | Example                                             |
| ---- | ------------------ | --------------------------------------------------- |
| -u   | Git repository url | https://github.com/docker-hy/ml-kurkkumopo-frontend |
| -t   | Docker image tag   | tomirantanen/ml-kurkkumopo-frontend                 |

### Docker daemon mount

Host system docker daemon is mounted to container with parameter:
`-v /var/run/docker.sock:/var/run/docker.sock`
This allows docker commands to be run inside container.

```
docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock \
    --env-file <path to env file> tomirantanen/docker-builder \
    -u <url> \
    -t <tag>
```
