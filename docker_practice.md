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
