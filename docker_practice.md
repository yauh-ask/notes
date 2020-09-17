`docker pull python:3.8` - to pull an image of python watching its layers pass.
`docker volume create <volume_name>` - to create a volume.
`docker inspect app_files` - to know the path of the volume to mount it on the container filesystem.
By using `docker run -it --name <name-of-the-container> -v <volume>:<container-path> <image> <command>` :

1. -it this is used to get an interactive terminal from the container

2. --name: you can specify the name of a container using this option

3. -v: this is used to bind volumes to the container filesystem.

Example: `docker run -it --name "first_container" -v /usercode/app_files:/app_files python:3.8 bash`

Write a program in the current_time.py file to print current time: `cd app_files && touch current_time.py`

Example:

import datetime, pytz

current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M:%S %z")

print(current_time)

The output:
python current_time.py 
16:46:10 +0530

To understand it better, create another container named ‘second_container’ from the Python 3.8 image and update the Python script located in ‘app_files’ volume to print the current date.

`docker run -it --name "second_container" -v /usercode/app_files:/app_files python:3.8 bash`
Example:

import datetime

current_date = datetime.datetime.now().strftime("%m-%d-%Y")

print(current_date)

The output:
python current_time.py 
04-26-2020


##### another example

- script file as date_time.py:

import datetime, pytz

c: Timezone can be changed to any allowed values.
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime(" %m.%d.%Y %H:%M:%S %z")

print(current_time)

- requirements file.txt
Comment: required Libraries
pytz==2018.7

- dockerfile
c: Base image to build

FROM python:3.8

c: Work directory specific to web IDE, You can change if you are running on your Local Machine
WORKDIR /exercise_2

c: COPY requirements.txt to container before running the code. This way any change in requirements will affect only one layer.

COPY requirements.txt requirements.txt

c: Install required libraries

RUN pip install -r requirements.txt

c: Add code file to container directory.
ADD . .

c: Running the code file. You can also use ENTRYPOINT here.
CMD [ "python", "date_time.py" ]


 P.S. Now that all dependencies are installed, we will copy our code files from the host machine to the container with ADD . . “.” represents the current directory of the host and container. Since we have already mentioned the WORKDIR, Docker will consider the WORKDIR as the current working directory.
Finally, we run our python script with CMD ["python", "date_time.py"]
