# Docker Networking

## Create a network with type as bridge and name webServers
```bash
docker network create --driver bridge webServers
```
## creating two weberwers based on Nginx image named web1 and web2
```bash
docker run -dit --name web1 --network webServers nginx bash
docker run -dit --name web2 --network webServers nginx bash
```
## connect to web2 and ping web1
```bash
docker exec -it web2 bash
apt update && apt install inetutils-ping -y
ping web1
```
#web1 = 172.19.0.2
#web2 = 172.19.0.3


## connect to web1 and ping web2
```bash
docker exec -it web1 bash
apt update && apt install inetutils-ping -y
ping web2
```
