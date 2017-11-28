import re

# for enigma only
procedurePattern = re.compile(r'^.*PROCEDURE\s*\(\s*\S+\s*\).*$')   # Enigma procedure
ownerPattern = re.compile(r'^.*(ENTITY|DATA_TYPE|PARENT)\s*\(\s*\S+\s*\).*$') # Enigma procedure owner

# process parsing here line by line
def parseFile(argFile):
    currentParent = ''
    for line in argFile:
        if ownerPattern.match(line):
            currentParent = re.sub(r'(.*(ENTITY|DATA_TYPE|PARENT)\s*\(|\s*\).*)', '', line)
        if procedurePattern.match(line):
            procedureName = re.sub(r'(.*PROCEDURE\s*\(|\s*\).*)', '', line)
        else:
            procedureName = ''
        if currentParent != '' and procedureName != '':
            print currentParent + '.' + procedureName