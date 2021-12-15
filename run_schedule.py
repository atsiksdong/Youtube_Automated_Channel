import os.path,glob,schedule,time,shutil
from video_downloader import run_func
from upload_to_youtube import upload_to_yt

def routine():
   try:
    run_func()
    for video in glob.glob('Videos\\*.mp4'):
        name = (os.path.basename(video))
        video_name = (os.path.basename(video).replace('.mp4',""))
        video_name = (os.path.basename(video_name).replace('%'," "))
        video_name = (os.path.basename(video_name).replace('%20'," "))
        video_name = (os.path.basename(video_name).replace('20%'," "))
        
        try:
         upload_to_yt(os.path.join('Videos\\',name),video_name)
         time.sleep(600)
         shutil.rmtree('Videos\\' , ignore_errors=False)
        except Exception as e:
            print(e)
   except Exception as e:
    print(e)

routine()

schedule.every(12).hours.do(routine)

while True:
    schedule.run_pending()
    time.sleep(1)
