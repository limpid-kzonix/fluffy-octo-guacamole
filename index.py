import docker

client = docker.DockerClient(base_url='unix://var/run/docker.sock')
container_list = client.containers.list()
for container in container_list:
    print(" [Container %s, ID %s] - %s" % (container.name, container.short_id, container.status.upper()))
