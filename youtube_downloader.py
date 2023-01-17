import youtube_dl
import os; os.chdir(r'C:\Users\user\Downloads')

url_input = {
    'https://www.youtube.com/watch?v=BaW_jenozKc': 'video',
    'https://www.youtube.com/watch?v=YhqsjUUHj6g': 'audio',
}

class MyLogger(object):
    def debug(self, msg):
        print(msg)
    def warning(self, msg):
        print(msg)
    def error(self, msg):
        print(msg)
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts_base = {
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
ydl_opts_audio = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
ydl_opts_video = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
}
ydl_opts_audio.update(ydl_opts_base)
ydl_opts_video.update(ydl_opts_base)

count = 0
for url, mode in url_input.items():
    count += 1
    print(f'\nProcessing URL {url} ({mode}, {count}/{len(url_input)})')
    with youtube_dl.YoutubeDL(ydl_opts_video if mode == 'video' else ydl_opts_audio) as ydl:
        ydl.download([url])
