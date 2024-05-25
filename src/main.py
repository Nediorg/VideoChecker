import yt_dlp
from time import sleep
import os
import requests
from config import *
from local import *

DESCRIPTION_TEXT = language.DESCRIPTION_TEXT
MESSAGE_TEXT = language.MESSAGE_TEXT
SUCCESS_TEXT = language.SUCCESS_TEXT
NEW_VIDEO_TEXT = language.NEW_VIDEO_TEXT
LOADING_TEXT = language.LOADING_TEXT
LOADING_VIDEO_TEXT = language.LOADING_VIDEO_TEXT
SENDING_TEXT = language.SENDING_TEXT
CLEANING_TEXT = language.CLEANING_TEXT
CLEANING_DISABLED_TEXT = language.CLEANING_DISABLED_TEXT
COOLDOWN_TEXT = language.COOLDOWN_TEXT
FIRST_LAUNCH_TEXT = language.FIRST_LAUNCH_TEXT

if not os.path.exists(videoPath):
    os.mkdir(videoPath)

def send_message(TOKEN, CHANNEL_ID, MESSAGE, VIDEO):
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
    with open(VIDEO, 'rb') as video_file:
        payload_video = {
            'chat_id': CHANNEL_ID,
            'caption': MESSAGE,
            'parse_mode': 'HTML'
        }
        files = {
            'video': video_file
        }
        response_video = requests.post(api_url, data=payload_video, files=files)
        log = response_video.json()
        print(log) if debugMode else ""

def get_video_ids(channel):
    ydl_opts = {
    'flat-playlist': True,
    'quiet': True,
    'extract_flat': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel, download=False)
        if 'entries' in result:
            video_ids = [entry['id'] for entry in result['entries']]
            return video_ids
        else:
            return []

def get_video_info(video_id):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
        return video_info

def download_video(video_url):
    ydl_opts = {
        'format': 'best',
        'n_threads': 10,
        'outtmpl': f'{videoPath}/%(title)s.%(ext)s',
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get('title', None)
        video_ext = info_dict.get('ext', None)
        video_filename = f"{video_title}.{video_ext}"
        video_full_path = os.path.join(videoPath, video_filename)
        return video_full_path

def video_scan(channel):
    videos = get_video_ids(channel + "/videos/")
    shorts = get_video_ids(channel + "/shorts/")
    video_list = videos + shorts
    if debugMode:
        print(video_list)
    return video_list

video_list = video_scan(youtubeChannel)

_FIRST_LAUNCH = True
while True:
    if not _FIRST_LAUNCH:
        temp_video_list = video_scan(youtubeChannel)
        new_videos = [video_id for video_id in temp_video_list if video_id not in video_list]
        if new_videos:
            print(NEW_VIDEO_TEXT)
            if debugMode:
                print(new_videos)
            for video_id in new_videos:
                video_info = get_video_info(video_id)
                video_name = video_info.get('title')
                print(LOADING_VIDEO_TEXT % {"video_name": video_name, "video_id": video_id})
                video_description = video_info.get('description')

                video_date = video_info.get('upload_date')
                video_date = f"{video_date[:4]}-{video_date[4:6]}-{video_date[6:]}"

                video_url = f'https://www.youtube.com/watch?v={video_id}'

                description = DESCRIPTION_TEXT % {"DESCRIPTION": video_description} if video_description != "" else ""
                MessageText = MESSAGE_TEXT % {"NAME": video_name, "DESCRIPTION": description, "DATE": video_date, "URL": video_url}

                print(LOADING_TEXT)
                video_file = download_video(video_url)
                print(SENDING_TEXT, end="\t")
                send_message(TELEGRAM_TOKEN, CHANNEL_ID, MessageText, video_file)
                print(SUCCESS_TEXT)
                if deleteTempFiles:
                    print(CLEANING_TEXT)
                    os.remove(video_file)
                else:
                    print(CLEANING_DISABLED_TEXT)

            print(COOLDOWN_TEXT % cooldown)
        video_list = temp_video_list
    else:
        print(FIRST_LAUNCH_TEXT + COOLDOWN_TEXT % cooldown)
    sleep(cooldown)
    _FIRST_LAUNCH = False
