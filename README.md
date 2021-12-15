# Youtube_Automated_Channel
Code to scrape , download and upload to youtube daily
## INSTRUCTIONS

   1. Download the Github Repository

   2. Download and install Python3 and pip if necessary.

   3. Install libraries with ```pip3 install -r requirements.txt``` or ```python3 -m pip install -r requirements.txt``` .

   4. Get setup and create a Project with the Youtube API: https://developers.google.com/youtube/v3/quickstart/python Be sure to follow it carefully, as it won't work if you don't do this part right. Download your OATH file and name it as ```client_secrets.json``` in your project folder.

   5. Run ```python3 run_schedule.py``` in your computer terminal (terminal or cmd). You have to sign in to your Youtube Account through the link the script will give you. It's going to ask you: "Please visit this URL to authorize this application:..." so you copy that link, paste it in your browser, and then sign into your Google account. Then paste the authentication code you get back into your terminal.
    
   6. Enjoy your fully automated youtube channel! :) Note that for uploading public videos, you have to complete an audit for the Youtube API. See the note in the Google Documentation. Without this, you can only post private videos, but they approve everyone. Have fun!
