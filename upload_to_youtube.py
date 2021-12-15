import os
from Google import Create_Service
from googleapiclient.http import MediaFileUpload


def upload_to_yt(file_name,video_name):
    CLIENT_SECRET_FILE = 'client_secrets.json'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': '{}'.format(video_name),
            'description': '',
            'tags': []
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload(file_name)

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()
    print('Video Uploaded')
    
