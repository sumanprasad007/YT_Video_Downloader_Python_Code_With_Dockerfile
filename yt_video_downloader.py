import pytube

# url = input("Enter your url: ")
url = "https://youtu.be/sn-HC7nSRKc"

path="C:"

pytube.YouTube(url).streams.get_highest_resolution().download(path)

