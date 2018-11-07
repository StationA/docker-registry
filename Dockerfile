FROM registry:2

ADD config.yml /etc/docker/registry/config.yml

EXPOSE 5000
