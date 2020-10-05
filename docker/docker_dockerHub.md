Why should we push images to Docker Hub? There are many reasons. Some of them are:

- Saves space: In the previous lesson “Troubleshooting in Docker”, we discussed the space issue. If we build our image and push it to Docker Hub, we don’t have to rebuild the image on production systems. This will save us a lot of space and time.
- Easy access: You can access your image from any other machine, provided you have an active internet connection.

Steps to push an image
1. type `docker login` on the command prompt or terminal
2. enter your login credentials
3. Tag the app image with your username, eg `docker tag flask_app:1.0 venky8283/flask_app:1.0`
4. Push the image using `docker push <username>/flask_app:1.0`


