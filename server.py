from fastapi import BackgroundTasks, FastAPI
from pytube import YouTube, Playlist
from pydantic import BaseModel
import os

app = FastAPI()


class Body(BaseModel):
    url: str

def download(link):

    p = Playlist(link)
    print(p.title)
    os.mkdir(p.title)
    for url in p.video_urls:
        print(url)
        youtube_object = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        youtube_object.bypass_age_gate()
        #youtube_object.bypass_age_gate("ANDROID") bypass_age_gate function might be changed
        print(youtube_object.title)
        youtube_object = youtube_object.streams.get_highest_resolution()

        try:
            youtube_object.download(output_path=f'./{p.title}')
        except:
            print("An error has occurred")

        print("Download is completed successfully")



@app.post("/")
async def send_notification(item:Body, background_tasks: BackgroundTasks):
    background_tasks.add_task(download, item.url)
    return {"message": "Download initated in the background"}
