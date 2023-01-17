import os; os.chdir(r'C:\path')

for filename in os.listdir():
    print(f'\n\n___Converting file: {filename}')
    os.system("ffmpeg -i \"" + filename + "\" -vn -ab 128k -ar 44100 -y \"..\\mp3\\" + filename.split(".")[0] + ".mp3\"")
