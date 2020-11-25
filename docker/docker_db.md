Running the Database Container

Steps to add the database:
- Pull MySQL server’s official Docker Hub image

- Run the image with MySQL environment variables

- Install the DB connector for the flask

- Change the application code

- Run the Flask app with a link to the database container

MySQL image

Type `docker pull mysql/mysql-server:5.7` to pull the MySQL image. Once the image is downloaded, let’s create a container from the image like this:
`docker run --name database mysql/mysql-server:5.7`

According to MySQL’s official documentation, we can configure MYSQL_ROOT_PASSWORD, MYSQL_USER, MYSQL_USER_PASSWORD, MYSQL_DATABASE from the command line 
while starting the container using environment variables passed to a container.

Running with ENV variables

`docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=backend -e MYSQL_USER=testuser -e MYSQL_PASSWORD=admin123 mysql/mysql-server:5.7`

The --name argument is used to define the container name.
`-e` is for environment variables. Each variable is used by MySQL in the startup script.

MYSQL_ROOT_PASSWORD=root: sets the root user’s password to ‘root’

MYSQL_DATABASE=backend: creates the database named ‘backend’ while starting up

MYSQL_USER=testuser: creates a non-root user to access the database

MYSQL_PASSWORD=admin123: set the non-root user’s password


Access the MySQL shell in the new command prompt/terminal by using the MySQL user and password we provided in the environment variables:

`docker exec -it mysql bash` followed by `mysql -u testuser -padmin123`
Try to check if the database is created or not using `show databases` query.

App and DB connectivity

`docker network ls & docker inspect <NETWORK ID> ` to look for the containers section.

Bridge network needs containers to be ‘linked’ to make DB reachable.
So, let’s link the DB container to our application container. First, stop the application container and rerun with:

`docker run --link "mysql:backenddb" -p 5000:5000 flask_app:1.0` and then, check.
`docker exec -it f9cf42e23825 bash`
`cat /etc/hosts`
`ping mysql`

To authenticate users, we need to create a table in that database. So, either you can execute SQL commands in init.sql directly from the SQL shell or
leverage Docker’s docker-entrypoint-initdb.d folder.

docker-entrypoint-initdb.d explanation

Any SQL script present in docker-entrypoint-initdb.d folder is executed by Docker as soon as a container is up and running. So, to leverage this feature, 
we will mount the db/init.sql file onto Docker’s initdb.d/ folder using -v argument while running the container and do the following:

- Stop the existing MySQL container
- Remove it using the Docker rm command
- Type `docker run --name mysql -d -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=backend -e MYSQL_USER=testuser -e MYSQL_PASSWORD=admin123 -v <Path/to/Project/>/Docker/db/init.sql:/docker-entrypoint-initdb.d/init.sql mysql/mysql-server:5.7`

We have just added two new things in the command:

-v <Path/to/Project/>/Docker/db/init.sql:/docker-entrypoint-initdb.d/init.sql to mount the DB startup script and -d to run the container in the background.

Next, stop the app container, build a new image for our new code docker build -t flask_app:2.0, and 
run using docker run --link "mysql:backenddb" -p 5000:5000 flask_app:1.0.

If everything goes well, you should be able to see the app and authenticate with `admin’ and ‘admin123’ as username and password respectively.

Summary of steps to add a database

1) Pull a Docker image of MySQL server
2) Create a SQL init script for the database
3) Run the database container with environment variables
4) Mount the init.sql script in the docker-entrypoint-init.db folder

*** The good news is docker-compose addresses this issue and automates these steps.
*** In short, Compose is a tool for defining and running multi-container Docker applications.
*** Modify the code and rerun app container with a link to the database container

Docker-compose installation

[Official Docs](https://docs.docker.com/compose/install/)

Linux 

Run this command to download the current stable release of Docker Compose 
`sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

Apply executable permissions to the binary with `sudo chmod +x /usr/local/bin/docker-compose`

Verify installation with `docker-compose --version`.

Docker-compose file

Modify mounts according to your files system. For example, 

volumes:
 - "/usercode/:/code"
 
 Here, replace ‘usercode’ directory to your directory where the project is cloned. 
 It can be something like /Users/Home/username/documents/Docker.

Then, open up the terminal and cd into the directory where docker-compose.yml file is present. Finally, hit `docker-compose up --build`.

