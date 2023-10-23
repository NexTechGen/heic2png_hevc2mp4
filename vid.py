import moviepy.editor as moviepy
import os

dir = "C:\\Users\WELCOME\heic2png\\vvv"
dir_list = os.listdir(dir)

print(len(dir_list))
c = 1
for name in dir_list:
    clip = moviepy.VideoFileClip(dir+"\\"+name)
    clip.write_videofile("C:\\Users\WELCOME\heic2png\kk\\"+name.split(".")[0]+".mp4")
    print(f'{c}.{name.split(".")[0]+".mp4"} saved')
    c += 1