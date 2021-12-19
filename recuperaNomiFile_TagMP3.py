
import os,shutil
import eyed3

path = os.environ['USERPROFILE']+"\\Desktop"
dirs = os.listdir(path)
cont = 0

for f in dirs:
    if ".mp3"in f:
        audiofile = eyed3.load(path+"\\"+f)
        try:
            print(audiofile.tag.artist)
            art = audiofile.tag.artist
            print(audiofile.tag.title)
            title = audiofile.tag.title
            ##newfile = open(art +" - "+title,"w")
            shutil.copy(path+"\\"+f, path+"\\"+art+" - "+title+".mp3" )
        except Exception:
            continue


