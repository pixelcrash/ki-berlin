# piA 192.168.1.121

from flask import Flask, render_template
from playsound import playsound
import pygame, os, os.path, glob, requests, shutil
from zipfile import ZipFile 


file = "ready.mp3"
pygame.mixer.init(48000, -16, 1, 1024)
pygame.mixer.music.load(file)
pygame.mixer.music.play()