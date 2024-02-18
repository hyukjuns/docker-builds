# Dockerfile Samples

```
# Container Monitoring
docker stats <CONTAINER_ID>

# Container Debug
docker inspect <CONTAINER_ID>

# Copy Files
docker cp <CONTAINER_ID>:<PATH> <HOST_PATH>

# Kill All Containers
docker rm -f $(docker ps -aq)

```
