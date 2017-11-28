#!/usr/bin/python
import re
import sys
import os
from actualParser import parseFile


#get value from config
def getConfigValue ( argValue ):
    value = re.search(r'(\'|\")+\s*.+\s*(\'|\")+', argValue)
    value = re.sub(r'\s*(\'|\")+\s*', '', value.group())
    return value

def searchFiles ( argDir , filesA, fileExt):
    try:
        for e in os.listdir(argDir + '/'):
            searchFiles(argDir + '/' + e, filesA, fileExt)
    except:
        if re.search(r''+ fileExt +'$', argDir):
            filesA.insert(len(filesA), argDir)

# MAIN
# read config file
try:
    inputfile = open('config.txt')
except:
    print 'config.txt cannot be found'
    sys.exit() 

#parse config file
config = inputfile.readlines()

source = getConfigValue(config[0])    # root folder of to-be-parsed code files
fileExt = getConfigValue(config[1])   # extension of the code files
filesA = []
searchFiles(source, filesA, fileExt)  # searches all files with the given root dir with the file extension given in config

functions = [] # will hold names of available functions/methods/procedures

# parse each file found
for f in filesA:
    with open(f, 'r') as damnFile:
        parseFile(damnFile)
        damnFile.close()