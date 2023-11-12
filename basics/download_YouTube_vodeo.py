"""
pytube
pytube is a genuine, lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.

Documentation
Detailed documentation about the usage of the library can be found at pytube.io. This is recommended for most cases. If you want to hastily download a single video, the quick start guide below might be what you're looking for.

Description
YouTube is the most popular video-sharing platform in the world and as a hacker, you may encounter a situation where you want to script something to download videos. For this, I present to you: pytube.

pytube is a lightweight library written in Python. It has no third-party dependencies and aims to be highly reliable.

pytube also makes pipelining easy, allowing you to specify callback functions for different download events, such as on progress or on complete.

Furthermore, pytube includes a command-line utility, allowing you to download videos right from the terminal.



Using the command-line interface
Using the CLI is remarkably straightforward as well. To download a video at the highest progressive quality, you can use the following command:

$ pytube https://youtube.com/watch?v=2lAe1cqCOXo
You can also do the same for a playlist:

$ pytube https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n

"""




from pytube import YouTube
link=input("Input the URL of a YouTube video you want to download  ")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()