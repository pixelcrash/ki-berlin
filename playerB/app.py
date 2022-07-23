# piA 192.168.1.125

from flask import Flask, render_template
from playsound import playsound
import pygame, os, os.path, glob, requests, shutil, time
from zipfile import ZipFile 

app = Flask(__name__)


file = "ready.mp3"
pygame.mixer.init(48000, -16, 1, 1024)
pygame.mixer.music.load(file)
pygame.mixer.music.play()
    

@app.route('/playertest')
def playertest():
    file = "ready.mp3"
    pygame.mixer.init(48000, -16, 1, 1024)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
    path = ('./audio/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.mp3'):
            x+=1
    
    return render_template('index.html', amount=x, msg="")

@app.route('/')
def index():

    

    path = ('./audio/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.mp3'):
            x+=1
            
    return render_template('index.html', amount=x, msg="")
    
@app.route('/reboot')
def reboot():
    os.system("sudo reboot")


@app.route('/playfile/<name>')
def play(name):
    file = "audio/" + name + ".mp3"
    pygame.mixer.init(48000, -16, 1, 1024)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
        
    path = ('./audio/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.mp3'):
            x+=1
            
    return render_template('index.html', amount=x, msg="Audio was played");
    
    
@app.route('/count')
def count():
    path = ('./audio/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.mp3'):
            x+=1
    return render_template('count.html', amount=x);
    

@app.route('/update')
def update():
    
    shutil.rmtree("./audio", ignore_errors=True)
    os.mkdir("./audio")
    
    url = 'http://ki.blist-apparat.at/B.zip'
    updateFile = "./audio/B.zip"
    
    r = requests.get(url, allow_redirects=True)
    open(updateFile, 'wb').write(r.content)
    
    with ZipFile(updateFile, 'r') as zip: 
        zip.printdir() 
        zip.extractall('./audio') 
    path = ('./audio/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.mp3'):
            x+=1
            
    file = "updated.mp3"
    pygame.mixer.init(48000, -16, 1, 1024)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
    return render_template('index.html', amount=x, msg="Your files were updated");

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
