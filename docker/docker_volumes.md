Whenever you create a container from an image, it creates a new container without any data except the image data.
Whenever a container is created, a file system is also created with it, which is a default Linux filesystem. Although Docker shares the OS’s kernel, there is a separation between file systems.

Commands:

- `docker volume --help`: to get the volume help
- `docker volume create`: to create a new volume
- `docker inspect volume`: to inspect the created volume
- `docker run -v`: to mount a volume

### Bind mount

This is available from a very early version of Docker. 
In bind mount, you use the host filesystem and mount it on the container using -v flag with the run command.

$docker run -it -v <absolute_path>:<folder path or new folder name> date_project:1.0

Bind mount has some limitations and is dependent on the host’s file system. If a folder is accidentally deleted from the host, Docker can’t do anything.

### Volumes

Docker volumes are mostly created to share data within different containers, rather than sharing data with host and container.
