# Youtube Video Downloader Docker Container
Introduction
This Docker container includes a script that uses the Pytube library to download Youtube videos. The script takes a Youtube video URL as input and downloads the highest resolution video to the designated file path.

# Requirements
Docker
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
