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

```bash
docker network create -d bridge --subnet 182.18.0.0/25 --gateway 182.18.0.1 dbNet

docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=db_pass1234 --name mysqlDB --network dbNet mysql:latest

docker run -dit --name u1 --network dbNet ubuntu bash
	apt update && apt install mysql-client
	#mysql -h mysqLDB -uroot -pdb_pass1234
	mysql -h mysqLDB -uroot -p
```
