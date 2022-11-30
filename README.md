# Py-spotify-downloader
# download songs from your spotify playlist from youtube!


prerequisites:
    1. your Spotify APPs ClientID
    2. your Spotify APPs ClientSecret
    
USE INSTRUCTIONS:
    1. start the included nginx install it is needed for the spotify redirect
       if you dont start it and the redirect dosent resolve you won't get a token
    
    2. open a terminal in the scripts working directory and type the following:
       Scripts\activate.bat
    
    2a. you terminal should look something like this now:
        (Py-spotify-downloader) D:\Py-spotify-downloader>
        that means yuo are ready to run the Script
    
    3. run py main.py

   | FAQ:                                                                                            |
   
   | Q: But I don't want to run nginx i dont want hunt nginx in task manager later to end the process|
   | A: Don't worry the script kills nginx when it exits                                             |
   
   | Q: Why do I need all this work for just running main.py can't i just install the dependecies    |
   |    with pip and run it?                                                                         |
   | A: Sadly no some these libraries were pretty broken and have patches done by me in them         |
   |    most of them have these exact patches in pull request by other people who were faster        |
   |    than me with making pull request but it seems none of them are in stable releases :(         |
