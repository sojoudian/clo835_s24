docker run -p 80:80 mcr.microsoft.com/azuredocs/aci-helloworld
docker run -d -p 80:80 mcr.microsoft.com/azuredocs/aci-helloworld
docker ps -a
docker stop a8a73651938d
docker start a8a73651938d
export K8S_COLOR=GREEN
docker images
docker pull nginx
docker images
docker rmi nginx
docker images
docker run -p 80:80 nginx
#Control+C to stop Nginx
docker run -d -p 80:80 nginx

cd week2
docker build -t pyhelloworld:0.1 .
docker run -p 8000:8000 pyhelloworld:0.1
