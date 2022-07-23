from pprint import pprint
from requests_futures.sessions import FuturesSession
import random
import requests
import urllib.request
import configparser
import time
import requests 
import sys 

# Change this data only
# This is the BRAIN PI  192.168.1.130
# This runs no Flask

# Session 
session = FuturesSession()

#use with waitwait function and multi 
timeoutmin = 2
timeoutmax = 3

#standard delay
delay = 2

req = requests.get("http://192.168.1.124:5000/count")
print("There are " + req.text + " Files on PlayerD")

# Playmode 1:100 
playModeWeight = 10
# Playmode Mix 
# f.e. 0-30 Single = 30%  Mix 50-30 = 20% 
# Pair mode is 100-50 = 50%  
playModeWeightMix = 80

#how many audio files
files = int(req.text)



# NO EDIT AFTER HERE -------------->
# End Change this data only


counter = 0
poss = 0
playerA = []
playerB = []
playerC = []
playerD = []
playerE = []
playerF = []

urlPlayerA = 'http://192.168.1.121:5000/playfile/'
urlPlayerB = 'http://192.168.1.125:5000/playfile/'
urlPlayerC = 'http://192.168.1.123:5000/playfile/'
urlPlayerD = 'http://192.168.1.124:5000/playfile/'
urlPlayerE = 'http://192.168.1.126:5000/playfile/'
urlPlayerF = 'http://192.168.1.127:5000/playfile/'

urlPlayerP = 'http://192.168.1.131:4444/print/'

playmode = 0
playcount = 0
played = [0, 0, 0, 0, 0, 0]
playthis = []

playlist = [['a','b','c','d','e','f'],['b','a','c','d','e','f'],['c','a','b','d','e','f'],['a','c','b','d','e','f'],['b','c','a','d','e','f'],['c','b','a','d','e','f'],['c','b','d','a','e','f'],['b','c','d','a','e','f'],['d','c','b','a','e','f'],['c','d','b','a','e','f'],['b','d','c','a','e','f'],['d','b','c','a','e','f'],['d','a','c','b','e','f'],['a','d','c','b','e','f'],['c','d','a','b','e','f'],['d','c','a','b','e','f'],['a','c','d','b','e','f'],['c','a','d','b','e','f'],['b','a','d','c','e','f'],['a','b','d','c','e','f'],['d','b','a','c','e','f'],['b','d','a','c','e','f'],['a','d','b','c','e','f'],['d','a','b','c','e','f'],['e','a','b','c','d','f'],['a','e','b','c','d','f'],['b','e','a','c','d','f'],['e','b','a','c','d','f'],['a','b','e','c','d','f'],['b','a','e','c','d','f'],['b','a','c','e','d','f'],['a','b','c','e','d','f'],['c','b','a','e','d','f'],['b','c','a','e','d','f'],['a','c','b','e','d','f'],['c','a','b','e','d','f'],['c','e','b','a','d','f'],['e','c','b','a','d','f'],['b','c','e','a','d','f'],['c','b','e','a','d','f'],['e','b','c','a','d','f'],['b','e','c','a','d','f'],['a','e','c','b','d','f'],['e','a','c','b','d','f'],['c','a','e','b','d','f'],['a','c','e','b','d','f'],['e','c','a','b','d','f'],['c','e','a','b','d','f'],['d','e','a','b','c','f'],['e','d','a','b','c','f'],['a','d','e','b','c','f'],['d','a','e','b','c','f'],['e','a','d','b','c','f'],['a','e','d','b','c','f'],['a','e','b','d','c','f'],['e','a','b','d','c','f'],['b','a','e','d','c','f'],['a','b','e','d','c','f'],['e','b','a','d','c','f'],['b','e','a','d','c','f'],['b','d','a','e','c','f'],['d','b','a','e','c','f'],['a','b','d','e','c','f'],['b','a','d','e','c','f'],['d','a','b','e','c','f'],['a','d','b','e','c','f'],['e','d','b','a','c','f'],['d','e','b','a','c','f'],['b','e','d','a','c','f'],['e','b','d','a','c','f'],['d','b','e','a','c','f'],['b','d','e','a','c','f'],['c','d','e','a','b','f'],['d','c','e','a','b','f'],['e','c','d','a','b','f'],['c','e','d','a','b','f'],['d','e','c','a','b','f'],['e','d','c','a','b','f'],['e','d','a','c','b','f'],['d','e','a','c','b','f'],['a','e','d','c','b','f'],['e','a','d','c','b','f'],['d','a','e','c','b','f'],['a','d','e','c','b','f'],['a','c','e','d','b','f'],['c','a','e','d','b','f'],['e','a','c','d','b','f'],['a','e','c','d','b','f'],['c','e','a','d','b','f'],['e','c','a','d','b','f'],['d','c','a','e','b','f'],['c','d','a','e','b','f'],['a','d','c','e','b','f'],['d','a','c','e','b','f'],['c','a','d','e','b','f'],['a','c','d','e','b','f'],['b','c','d','e','a','f'],['c','b','d','e','a','f'],['d','b','c','e','a','f'],['b','d','c','e','a','f'],['c','d','b','e','a','f'],['d','c','b','e','a','f'],['d','c','e','b','a','f'],['c','d','e','b','a','f'],['e','d','c','b','a','f'],['d','e','c','b','a','f'],['c','e','d','b','a','f'],['e','c','d','b','a','f'],['e','b','d','c','a','f'],['b','e','d','c','a','f'],['d','e','b','c','a','f'],['e','d','b','c','a','f'],['b','d','e','c','a','f'],['d','b','e','c','a','f'],['c','b','e','d','a','f'],['b','c','e','d','a','f'],['e','c','b','d','a','f'],['c','e','b','d','a','f'],['b','e','c','d','a','f'],['e','b','c','d','a','f'],['e','b','c','d','f','a'],['b','e','c','d','f','a'],['c','e','b','d','f','a'],['e','c','b','d','f','a'],['b','c','e','d','f','a'],['c','b','e','d','f','a'],['c','b','d','e','f','a'],['b','c','d','e','f','a'],['d','c','b','e','f','a'],['c','d','b','e','f','a'],['b','d','c','e','f','a'],['d','b','c','e','f','a'],['d','e','c','b','f','a'],['e','d','c','b','f','a'],['c','d','e','b','f','a'],['d','c','e','b','f','a'],['e','c','d','b','f','a'],['c','e','d','b','f','a'],['b','e','d','c','f','a'],['e','b','d','c','f','a'],['d','b','e','c','f','a'],['b','d','e','c','f','a'],['e','d','b','c','f','a'],['d','e','b','c','f','a'],['f','e','b','c','d','a'],['e','f','b','c','d','a'],['b','f','e','c','d','a'],['f','b','e','c','d','a'],['e','b','f','c','d','a'],['b','e','f','c','d','a'],['b','e','c','f','d','a'],['e','b','c','f','d','a'],['c','b','e','f','d','a'],['b','c','e','f','d','a'],['e','c','b','f','d','a'],['c','e','b','f','d','a'],['c','f','b','e','d','a'],['f','c','b','e','d','a'],['b','c','f','e','d','a'],['c','b','f','e','d','a'],['f','b','c','e','d','a'],['b','f','c','e','d','a'],['e','f','c','b','d','a'],['f','e','c','b','d','a'],['c','e','f','b','d','a'],['e','c','f','b','d','a'],['f','c','e','b','d','a'],['c','f','e','b','d','a'],['d','f','e','b','c','a'],['f','d','e','b','c','a'],['e','d','f','b','c','a'],['d','e','f','b','c','a'],['f','e','d','b','c','a'],['e','f','d','b','c','a'],['e','f','b','d','c','a'],['f','e','b','d','c','a'],['b','e','f','d','c','a'],['e','b','f','d','c','a'],['f','b','e','d','c','a'],['b','f','e','d','c','a'],['b','d','e','f','c','a'],['d','b','e','f','c','a'],['e','b','d','f','c','a'],['b','e','d','f','c','a'],['d','e','b','f','c','a'],['e','d','b','f','c','a'],['f','d','b','e','c','a'],['d','f','b','e','c','a'],['b','f','d','e','c','a'],['f','b','d','e','c','a'],['d','b','f','e','c','a'],['b','d','f','e','c','a'],['c','d','f','e','b','a'],['d','c','f','e','b','a'],['f','c','d','e','b','a'],['c','f','d','e','b','a'],['d','f','c','e','b','a'],['f','d','c','e','b','a'],['f','d','e','c','b','a'],['d','f','e','c','b','a'],['e','f','d','c','b','a'],['f','e','d','c','b','a'],['d','e','f','c','b','a'],['e','d','f','c','b','a'],['e','c','f','d','b','a'],['c','e','f','d','b','a'],['f','e','c','d','b','a'],['e','f','c','d','b','a'],['c','f','e','d','b','a'],['f','c','e','d','b','a'],['d','c','e','f','b','a'],['c','d','e','f','b','a'],['e','d','c','f','b','a'],['d','e','c','f','b','a'],['c','e','d','f','b','a'],['e','c','d','f','b','a'],['b','c','d','f','e','a'],['c','b','d','f','e','a'],['d','b','c','f','e','a'],['b','d','c','f','e','a'],['c','d','b','f','e','a'],['d','c','b','f','e','a'],['d','c','f','b','e','a'],['c','d','f','b','e','a'],['f','d','c','b','e','a'],['d','f','c','b','e','a'],['c','f','d','b','e','a'],['f','c','d','b','e','a'],['f','b','d','c','e','a'],['b','f','d','c','e','a'],['d','f','b','c','e','a'],['f','d','b','c','e','a'],['b','d','f','c','e','a'],['d','b','f','c','e','a'],['c','b','f','d','e','a'],['b','c','f','d','e','a'],['f','c','b','d','e','a'],['c','f','b','d','e','a'],['b','f','c','d','e','a'],['f','b','c','d','e','a'],['f','b','c','a','e','d'],['b','f','c','a','e','d'],['c','f','b','a','e','d'],['f','c','b','a','e','d'],['b','c','f','a','e','d'],['c','b','f','a','e','d'],['c','b','a','f','e','d'],['b','c','a','f','e','d'],['a','c','b','f','e','d'],['c','a','b','f','e','d'],['b','a','c','f','e','d'],['a','b','c','f','e','d'],['a','f','c','b','e','d'],['f','a','c','b','e','d'],['c','a','f','b','e','d'],['a','c','f','b','e','d'],['f','c','a','b','e','d'],['c','f','a','b','e','d'],['b','f','a','c','e','d'],['f','b','a','c','e','d'],['a','b','f','c','e','d'],['b','a','f','c','e','d'],['f','a','b','c','e','d'],['a','f','b','c','e','d'],['e','f','b','c','a','d'],['f','e','b','c','a','d'],['b','e','f','c','a','d'],['e','b','f','c','a','d'],['f','b','e','c','a','d'],['b','f','e','c','a','d'],['b','f','c','e','a','d'],['f','b','c','e','a','d'],['c','b','f','e','a','d'],['b','c','f','e','a','d'],['f','c','b','e','a','d'],['c','f','b','e','a','d'],['c','e','b','f','a','d'],['e','c','b','f','a','d'],['b','c','e','f','a','d'],['c','b','e','f','a','d'],['e','b','c','f','a','d'],['b','e','c','f','a','d'],['f','e','c','b','a','d'],['e','f','c','b','a','d'],['c','f','e','b','a','d'],['f','c','e','b','a','d'],['e','c','f','b','a','d'],['c','e','f','b','a','d'],['a','e','f','b','c','d'],['e','a','f','b','c','d'],['f','a','e','b','c','d'],['a','f','e','b','c','d'],['e','f','a','b','c','d'],['f','e','a','b','c','d'],['f','e','b','a','c','d'],['e','f','b','a','c','d'],['b','f','e','a','c','d'],['f','b','e','a','c','d'],['e','b','f','a','c','d'],['b','e','f','a','c','d'],['b','a','f','e','c','d'],['a','b','f','e','c','d'],['f','b','a','e','c','d'],['b','f','a','e','c','d'],['a','f','b','e','c','d'],['f','a','b','e','c','d'],['e','a','b','f','c','d'],['a','e','b','f','c','d'],['b','e','a','f','c','d'],['e','b','a','f','c','d'],['a','b','e','f','c','d'],['b','a','e','f','c','d'],['c','a','e','f','b','d'],['a','c','e','f','b','d'],['e','c','a','f','b','d'],['c','e','a','f','b','d'],['a','e','c','f','b','d'],['e','a','c','f','b','d'],['e','a','f','c','b','d'],['a','e','f','c','b','d'],['f','e','a','c','b','d'],['e','f','a','c','b','d'],['a','f','e','c','b','d'],['f','a','e','c','b','d'],['f','c','e','a','b','d'],['c','f','e','a','b','d'],['e','f','c','a','b','d'],['f','e','c','a','b','d'],['c','e','f','a','b','d'],['e','c','f','a','b','d'],['a','c','f','e','b','d'],['c','a','f','e','b','d'],['f','a','c','e','b','d'],['a','f','c','e','b','d'],['c','f','a','e','b','d'],['f','c','a','e','b','d'],['b','c','a','e','f','d'],['c','b','a','e','f','d'],['a','b','c','e','f','d'],['b','a','c','e','f','d'],['c','a','b','e','f','d'],['a','c','b','e','f','d'],['a','c','e','b','f','d'],['c','a','e','b','f','d'],['e','a','c','b','f','d'],['a','e','c','b','f','d'],['c','e','a','b','f','d'],['e','c','a','b','f','d'],['e','b','a','c','f','d'],['b','e','a','c','f','d'],['a','e','b','c','f','d'],['e','a','b','c','f','d'],['b','a','e','c','f','d'],['a','b','e','c','f','d'],['c','b','e','a','f','d'],['b','c','e','a','f','d'],['e','c','b','a','f','d'],['c','e','b','a','f','d'],['b','e','c','a','f','d'],['e','b','c','a','f','d'],['e','b','d','a','f','c'],['b','e','d','a','f','c'],['d','e','b','a','f','c'],['e','d','b','a','f','c'],['b','d','e','a','f','c'],['d','b','e','a','f','c'],['d','b','a','e','f','c'],['b','d','a','e','f','c'],['a','d','b','e','f','c'],['d','a','b','e','f','c'],['b','a','d','e','f','c'],['a','b','d','e','f','c'],['a','e','d','b','f','c'],['e','a','d','b','f','c'],['d','a','e','b','f','c'],['a','d','e','b','f','c'],['e','d','a','b','f','c'],['d','e','a','b','f','c'],['b','e','a','d','f','c'],['e','b','a','d','f','c'],['a','b','e','d','f','c'],['b','a','e','d','f','c'],['e','a','b','d','f','c'],['a','e','b','d','f','c'],['f','e','b','d','a','c'],['e','f','b','d','a','c'],['b','f','e','d','a','c'],['f','b','e','d','a','c'],['e','b','f','d','a','c'],['b','e','f','d','a','c'],['b','e','d','f','a','c'],['e','b','d','f','a','c'],['d','b','e','f','a','c'],['b','d','e','f','a','c'],['e','d','b','f','a','c'],['d','e','b','f','a','c'],['d','f','b','e','a','c'],['f','d','b','e','a','c'],['b','d','f','e','a','c'],['d','b','f','e','a','c'],['f','b','d','e','a','c'],['b','f','d','e','a','c'],['e','f','d','b','a','c'],['f','e','d','b','a','c'],['d','e','f','b','a','c'],['e','d','f','b','a','c'],['f','d','e','b','a','c'],['d','f','e','b','a','c'],['a','f','e','b','d','c'],['f','a','e','b','d','c'],['e','a','f','b','d','c'],['a','e','f','b','d','c'],['f','e','a','b','d','c'],['e','f','a','b','d','c'],['e','f','b','a','d','c'],['f','e','b','a','d','c'],['b','e','f','a','d','c'],['e','b','f','a','d','c'],['f','b','e','a','d','c'],['b','f','e','a','d','c'],['b','a','e','f','d','c'],['a','b','e','f','d','c'],['e','b','a','f','d','c'],['b','e','a','f','d','c'],['a','e','b','f','d','c'],['e','a','b','f','d','c'],['f','a','b','e','d','c'],['a','f','b','e','d','c'],['b','f','a','e','d','c'],['f','b','a','e','d','c'],['a','b','f','e','d','c'],['b','a','f','e','d','c'],['d','a','f','e','b','c'],['a','d','f','e','b','c'],['f','d','a','e','b','c'],['d','f','a','e','b','c'],['a','f','d','e','b','c'],['f','a','d','e','b','c'],['f','a','e','d','b','c'],['a','f','e','d','b','c'],['e','f','a','d','b','c'],['f','e','a','d','b','c'],['a','e','f','d','b','c'],['e','a','f','d','b','c'],['e','d','f','a','b','c'],['d','e','f','a','b','c'],['f','e','d','a','b','c'],['e','f','d','a','b','c'],['d','f','e','a','b','c'],['f','d','e','a','b','c'],['a','d','e','f','b','c'],['d','a','e','f','b','c'],['e','a','d','f','b','c'],['a','e','d','f','b','c'],['d','e','a','f','b','c'],['e','d','a','f','b','c'],['b','d','a','f','e','c'],['d','b','a','f','e','c'],['a','b','d','f','e','c'],['b','a','d','f','e','c'],['d','a','b','f','e','c'],['a','d','b','f','e','c'],['a','d','f','b','e','c'],['d','a','f','b','e','c'],['f','a','d','b','e','c'],['a','f','d','b','e','c'],['d','f','a','b','e','c'],['f','d','a','b','e','c'],['f','b','a','d','e','c'],['b','f','a','d','e','c'],['a','f','b','d','e','c'],['f','a','b','d','e','c'],['b','a','f','d','e','c'],['a','b','f','d','e','c'],['d','b','f','a','e','c'],['b','d','f','a','e','c'],['f','d','b','a','e','c'],['d','f','b','a','e','c'],['b','f','d','a','e','c'],['f','b','d','a','e','c'],['f','c','d','a','e','b'],['c','f','d','a','e','b'],['d','f','c','a','e','b'],['f','d','c','a','e','b'],['c','d','f','a','e','b'],['d','c','f','a','e','b'],['d','c','a','f','e','b'],['c','d','a','f','e','b'],['a','d','c','f','e','b'],['d','a','c','f','e','b'],['c','a','d','f','e','b'],['a','c','d','f','e','b'],['a','f','d','c','e','b'],['f','a','d','c','e','b'],['d','a','f','c','e','b'],['a','d','f','c','e','b'],['f','d','a','c','e','b'],['d','f','a','c','e','b'],['c','f','a','d','e','b'],['f','c','a','d','e','b'],['a','c','f','d','e','b'],['c','a','f','d','e','b'],['f','a','c','d','e','b'],['a','f','c','d','e','b'],['e','f','c','d','a','b'],['f','e','c','d','a','b'],['c','e','f','d','a','b'],['e','c','f','d','a','b'],['f','c','e','d','a','b'],['c','f','e','d','a','b'],['c','f','d','e','a','b'],['f','c','d','e','a','b'],['d','c','f','e','a','b'],['c','d','f','e','a','b'],['f','d','c','e','a','b'],['d','f','c','e','a','b'],['d','e','c','f','a','b'],['e','d','c','f','a','b'],['c','d','e','f','a','b'],['d','c','e','f','a','b'],['e','c','d','f','a','b'],['c','e','d','f','a','b'],['f','e','d','c','a','b'],['e','f','d','c','a','b'],['d','f','e','c','a','b'],['f','d','e','c','a','b'],['e','d','f','c','a','b'],['d','e','f','c','a','b'],['a','e','f','c','d','b'],['e','a','f','c','d','b'],['f','a','e','c','d','b'],['a','f','e','c','d','b'],['e','f','a','c','d','b'],['f','e','a','c','d','b'],['f','e','c','a','d','b'],['e','f','c','a','d','b'],['c','f','e','a','d','b'],['f','c','e','a','d','b'],['e','c','f','a','d','b'],['c','e','f','a','d','b'],['c','a','f','e','d','b'],['a','c','f','e','d','b'],['f','c','a','e','d','b'],['c','f','a','e','d','b'],['a','f','c','e','d','b'],['f','a','c','e','d','b'],['e','a','c','f','d','b'],['a','e','c','f','d','b'],['c','e','a','f','d','b'],['e','c','a','f','d','b'],['a','c','e','f','d','b'],['c','a','e','f','d','b'],['d','a','e','f','c','b'],['a','d','e','f','c','b'],['e','d','a','f','c','b'],['d','e','a','f','c','b'],['a','e','d','f','c','b'],['e','a','d','f','c','b'],['e','a','f','d','c','b'],['a','e','f','d','c','b'],['f','e','a','d','c','b'],['e','f','a','d','c','b'],['a','f','e','d','c','b'],['f','a','e','d','c','b'],['f','d','e','a','c','b'],['d','f','e','a','c','b'],['e','f','d','a','c','b'],['f','e','d','a','c','b'],['d','e','f','a','c','b'],['e','d','f','a','c','b'],['a','d','f','e','c','b'],['d','a','f','e','c','b'],['f','a','d','e','c','b'],['a','f','d','e','c','b'],['d','f','a','e','c','b'],['f','d','a','e','c','b'],['c','d','a','e','f','b'],['d','c','a','e','f','b'],['a','c','d','e','f','b'],['c','a','d','e','f','b'],['d','a','c','e','f','b'],['a','d','c','e','f','b'],['a','d','e','c','f','b'],['d','a','e','c','f','b'],['e','a','d','c','f','b'],['a','e','d','c','f','b'],['d','e','a','c','f','b'],['e','d','a','c','f','b'],['e','c','a','d','f','b'],['c','e','a','d','f','b'],['a','e','c','d','f','b'],['e','a','c','d','f','b'],['c','a','e','d','f','b'],['a','c','e','d','f','b'],['d','c','e','a','f','b'],['c','d','e','a','f','b'],['e','d','c','a','f','b'],['d','e','c','a','f','b'],['c','e','d','a','f','b'],['e','c','d','a','f','b'],['b','c','d','a','f','e'],['c','b','d','a','f','e'],['d','b','c','a','f','e'],['b','d','c','a','f','e'],['c','d','b','a','f','e'],['d','c','b','a','f','e'],['d','c','a','b','f','e'],['c','d','a','b','f','e'],['a','d','c','b','f','e'],['d','a','c','b','f','e'],['c','a','d','b','f','e'],['a','c','d','b','f','e'],['a','b','d','c','f','e'],['b','a','d','c','f','e'],['d','a','b','c','f','e'],['a','d','b','c','f','e'],['b','d','a','c','f','e'],['d','b','a','c','f','e'],['c','b','a','d','f','e'],['b','c','a','d','f','e'],['a','c','b','d','f','e'],['c','a','b','d','f','e'],['b','a','c','d','f','e'],['a','b','c','d','f','e'],['f','b','c','d','a','e'],['b','f','c','d','a','e'],['c','f','b','d','a','e'],['f','c','b','d','a','e'],['b','c','f','d','a','e'],['c','b','f','d','a','e'],['c','b','d','f','a','e'],['b','c','d','f','a','e'],['d','c','b','f','a','e'],['c','d','b','f','a','e'],['b','d','c','f','a','e'],['d','b','c','f','a','e'],['d','f','c','b','a','e'],['f','d','c','b','a','e'],['c','d','f','b','a','e'],['d','c','f','b','a','e'],['f','c','d','b','a','e'],['c','f','d','b','a','e'],['b','f','d','c','a','e'],['f','b','d','c','a','e'],['d','b','f','c','a','e'],['b','d','f','c','a','e'],['f','d','b','c','a','e'],['d','f','b','c','a','e'],['a','f','b','c','d','e'],['f','a','b','c','d','e'],['b','a','f','c','d','e'],['a','b','f','c','d','e'],['f','b','a','c','d','e'],['b','f','a','c','d','e'],['b','f','c','a','d','e'],['f','b','c','a','d','e'],['c','b','f','a','d','e'],['b','c','f','a','d','e'],['f','c','b','a','d','e'],['c','f','b','a','d','e'],['c','a','b','f','d','e'],['a','c','b','f','d','e'],['b','c','a','f','d','e'],['c','b','a','f','d','e'],['a','b','c','f','d','e'],['b','a','c','f','d','e'],['f','a','c','b','d','e'],['a','f','c','b','d','e'],['c','f','a','b','d','e'],['f','c','a','b','d','e'],['a','c','f','b','d','e'],['c','a','f','b','d','e'],['d','a','f','b','c','e'],['a','d','f','b','c','e'],['f','d','a','b','c','e'],['d','f','a','b','c','e'],['a','f','d','b','c','e'],['f','a','d','b','c','e'],['f','a','b','d','c','e'],['a','f','b','d','c','e'],['b','f','a','d','c','e'],['f','b','a','d','c','e'],['a','b','f','d','c','e'],['b','a','f','d','c','e'],['b','d','f','a','c','e'],['d','b','f','a','c','e'],['f','b','d','a','c','e'],['b','f','d','a','c','e'],['d','f','b','a','c','e'],['f','d','b','a','c','e'],['a','d','b','f','c','e'],['d','a','b','f','c','e'],['b','a','d','f','c','e'],['a','b','d','f','c','e'],['d','b','a','f','c','e'],['b','d','a','f','c','e'],['c','d','a','f','b','e'],['d','c','a','f','b','e'],['a','c','d','f','b','e'],['c','a','d','f','b','e'],['d','a','c','f','b','e'],['a','d','c','f','b','e'],['a','d','f','c','b','e'],['d','a','f','c','b','e'],['f','a','d','c','b','e'],['a','f','d','c','b','e'],['d','f','a','c','b','e'],['f','d','a','c','b','e'],['f','c','a','d','b','e'],['c','f','a','d','b','e'],['a','f','c','d','b','e'],['f','a','c','d','b','e'],['c','a','f','d','b','e'],['a','c','f','d','b','e'],['d','c','f','a','b','e'],['c','d','f','a','b','e'],['f','d','c','a','b','e'],['d','f','c','a','b','e'],['c','f','d','a','b','e'],['f','c','d','a','b','e']]


#functions
def fillArrayA():
  for i  in range(0,files):
    playerA.append(int(i) + 1)
    
def fillArrayB():
  for i  in range(0,files):
    playerB.append(int(i) + 1)
    
def fillArrayC():
  for i  in range(0,files):
    playerC.append(int(i) + 1)
    
def fillArrayD():
  for i  in range(0, files):
    playerD.append(int(i) + 1)
    
def fillArrayE():
  for i  in range(0, files):
    playerE.append(int(i) + 1)

def fillArrayF():
  for i  in range(0, files):
    playerF.append(int(i) + 1)
    
def getFiles():
    played[0] = random.choice(playerA)
    played[1] = random.choice(playerB)
    played[2] = random.choice(playerC)
    played[3] = random.choice(playerD)
    played[4] = random.choice(playerE)
    played[5] = random.choice(playerF)
    
def printTheFile(printit):
    url = urlPlayerP + str(printit)
    session.get(url)
    print('print file: ', printit)
    
def playfile(pi, audiofile):
    if(pi == 'a'):
        url = urlPlayerA + str(audiofile)
    elif(pi == 'b'):
        url = urlPlayerB + str(audiofile)
    elif(pi == 'c'):
        url = urlPlayerC + str(audiofile)
    elif(pi == 'd'):
        url = urlPlayerD + str(audiofile)
    elif(pi == 'e'):
        url = urlPlayerE + str(audiofile)
    elif(pi == 'f'):
        url = urlPlayerF + str(audiofile)

    session.get(url)

def waitwait(multi = 1):
    delay = random.uniform(timeoutmin, timeoutmax)
    delay = delay * multi
    print('Wait ', delay)
    time.sleep(delay)

# Fill array with 
fillArrayA()
fillArrayB()
fillArrayC()
fillArrayD()
fillArrayE()
fillArrayF()

# Loop
while True:
  
  playmode = random.randint(0,100)
  print('Playmode random: ', playmode)
  
  playthis = random.choice(playlist)
  #get files
  getFiles()
  
  contains_duplicates = len(played) != len(set(played))
  
  if(contains_duplicates):
      getFiles()      
  
  if(playmode < playModeWeight):
    # Pair Mode
    print('--> PAIR Mode')
    print('Speaker Order: ', playthis)
    print('Playlist:', played)
    playfile(playthis[0], played[0])
    playfile(playthis[1], played[1])
    waitwait(2)
    playfile(playthis[2], played[2])
    playfile(playthis[3], played[3])
    waitwait(2)
    playfile(playthis[4], played[4])
    playfile(playthis[5], played[5])
    waitwait(2)

  elif(playmode > playModeWeight and playmode < playModeWeightMix):
    # Single Mode
    print('--> SINGLE Mode')
    print('Speaker Order: ', playthis)
    print('Playlist:', played)
    playfile(playthis[0], played[0])
    waitwait(1)
    playfile(playthis[1], played[1])
    waitwait(1)
    playfile(playthis[2], played[2])
    waitwait(1)
    playfile(playthis[3], played[3])
    waitwait(0.5)
    playfile(playthis[4], played[4])
    waitwait(0.5)
    playfile(playthis[5], played[5])
    waitwait(0.5)
  
    
  elif(playmode > playModeWeightMix):
    
    # Single Mode
    print('--> MIX Mode')
    print('Speaker Order: ', playthis)
    print('Playlist:', played)
    mixmode = random.randint(1, 4)
    
    if(mixmode == 1):
        playfile(playthis[0], played[0])
        waitwait(1)
        playfile(playthis[1], played[1])
        playfile(playthis[2], played[2])
        waitwait(1)
        playfile(playthis[3], played[3])
        waitwait(1)
        playfile(playthis[4], played[4])
        playfile(playthis[5], played[5])
        waitwait(0.5)
        
    elif(mixmode == 2):
        playfile(playthis[0], played[0])
        playfile(playthis[1], played[1])
        waitwait()
        playfile(playthis[2], played[2])
        waitwait(1.5)
        playfile(playthis[3], played[3])
        waitwait(1)
        playfile(playthis[4], played[4])
        waitwait(1)
        playfile(playthis[5], played[5])
        waitwait(0.5)
        
    elif(mixmode == 3):
        playfile(playthis[0], played[0])
        waitwait()
        playfile(playthis[1], played[1])
        waitwait()
        playfile(playthis[2], played[2])
        playfile(playthis[3], played[3])
        waitwait(1)
        playfile(playthis[4], played[4])
        waitwait(1)
        playfile(playthis[5], played[5])
        waitwait(0.5)
        
    elif(mixmode == 4):
        playfile(playthis[0], played[0])
        playfile(playthis[1], played[1])
        waitwait()
        playfile(playthis[2], played[2])
        waitwait()
        playfile(playthis[3], played[3])
        waitwait(1)
        playfile(playthis[4], played[4])
        waitwait(1)
        playfile(playthis[5], played[5])
        waitwait(0.5)
    
    
  #random print file from array
  printfile = random.choice(played)
  printTheFile(printfile)
  
  playerA.remove(played[0])
  playerB.remove(played[1])
  playerC.remove(played[2])
  playerD.remove(played[3])
  playerE.remove(played[4])
  playerF.remove(played[5])
  
  counter += 1
  poss += 1
  
  if(counter == files):
      fillArrayA()
      fillArrayB()
      fillArrayC()
      fillArrayD()
      fillArrayE()
      fillArrayF()
      print('counter refill----------------------------------------------------')
      counter = 0
      
  print('--------------------------')
  waitwait(1)
  
  