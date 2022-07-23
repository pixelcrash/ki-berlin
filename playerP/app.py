# This is the printer PI
# 192.168.1.131

from flask import Flask, render_template
import os, os.path, glob, requests, shutil
from escpos.printer import Usb
from zipfile import ZipFile 

app = Flask(__name__)

@app.route('/')
def index():
    path = ('./text/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.txt'):
            x+=1
    return render_template('index.html', amount=x, msg="")
    
    
@app.route('/reboot')
def reboot():    
    os.system("sudo reboot")
    

@app.route('/amount')
def amount():
    path = ('./text/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.txt'):
            x+=1
    return render_template('count.html', amount=x)
    

@app.route('/print/<name>')
def prints(name):
    txtFile = "text/" + name + ".txt"
    path = ('./text/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.txt'):
            x+=1

    with open(txtFile) as f:
        first_line = f.readline()
        p = Usb(0x0483, 0x5743)
        p.set(align="CENTER")
        p.text("\n \n \n \n \n")
        p.text(first_line)
        p.text("\n \n \n \n \n")

    return render_template('index.html', amount=x, msg="Text was printed")

@app.route('/update')
def update():

    path = ('./text/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.txt'):
            x+=1

    shutil.rmtree("./text", ignore_errors=True)
    os.mkdir("./text")
    url = 'http://ki.blist-apparat.at/T.zip'
    r = requests.get(url, allow_redirects=True)
    open('./text/T.zip', 'wb').write(r.content)

    with ZipFile('./text/T.zip', 'r') as zip: 
        zip.printdir() 
        zip.extractall('./text') 

    return render_template('index.html', amount=x, msg="Text files are updated")


@app.route('/count')
def count():
    path = ('./text/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.txt'):
            x+=1
    return render_template('index.html', amount=x, msg="Files counted")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='4444')
