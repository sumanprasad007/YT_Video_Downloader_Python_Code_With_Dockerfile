# Youtube Video Downloader Docker Container
Introduction
This Docker container includes a script that uses the Pytube library to download Youtube videos. The script takes a Youtube video URL as input and downloads the highest resolution video to the designated file path.

# Code Explaination:

The code imports the Pytube library and sets a default Youtube video URL to be used as an example. The URL is passed as a parameter to the YouTube method of the Pytube library, which returns a stream of the video. The highest resolution video stream is then selected and downloaded to the file path specified by the path variable (currently set to "C:").

The code can be run in a Docker container to download the Youtube video, which provides an isolated environment for the script to run in. The Docker container can be created by building a Docker image using the provided Dockerfile and running the image as a container. The end-user will enter the Youtube video URL when prompted by the script running inside the container.

# Requirements
Docker

# Dockerfile Explaination:
The Dockerfile specifies the steps to build a Docker image for a Python application.

FROM python:3.8-alpine: This line specifies the base image to be used for the Docker image. In this case, it is using the latest version of Python (3.8) on an Alpine Linux base image.

COPY . /app: This line copies all the files in the current directory to a new directory named /app in the Docker image.

WORKDIR /app: This line sets the working directory for the subsequent steps in the Dockerfile to /app.

RUN pip install -r requirements.txt: This line runs the command pip install -r requirements.txt inside the Docker image. This command installs the dependencies specified in the requirements.txt file.

CMD [ "python","yt_video_downloader.py" ]: This line sets the default command that will be run when a container is created from the image. The command [ "python","yt_video_downloader.py" ] runs the script yt_video_downloader.py using the Python interpreter.

In summary, the Dockerfile builds an image based on the Alpine Linux distribution with Python 3.8 installed, copies all the files in the current directory to the /app directory in the image, sets the working directory to /app, installs the dependencies specified in the requirements.txt file, and sets the default command to run the yt_video_downloader.py script using the Python interpreter.

Usage
# Clone the repository
Navigate to the directory where the Dockerfile is located
Build the Docker image using the following command:

docker build -t <image-name> .
Run the Docker container using the following command:

docker run -it <image-name>

Enter the Youtube video URL when prompted.
The video will be downloaded to the path specified in the script (currently set to "C:").

# Note
The path can be changed by modifying the path variable in the script.
