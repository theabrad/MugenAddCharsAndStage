import os
import glob
import wx

directory = os.getcwd()							#get the directory
select = 'select.def'							#select.def file

#Name Directories
charDir = directory + '\\chars'					#Folder for characters
stageDir = directory + '\\stages'				#Folder for stages
selectDir = directory + '\\data'				#Folder for select.def
musicDir = directory + '\\sound'				#Folder for Music


#get the list of characters
def getChars():
	charList =  [f for f in os.listdir(charDir)
            	if os.path.isdir(os.path.join(charDir, f))]
	return charList

#get the list of stages
def getStages():
	os.chdir(stageDir)							#change the directory to the stage directory
	stageName = glob.glob('*.def')				#search for only the .def files
	return stageName

#get all of the music files
def getMusic():
	os.chdir(musicDir)
	musicList = glob.glob('*.mp3')
	return musicList

#add a char to select.def function
def addChar(character, stage):
	if (stage == ''):
		file.write("{0}\n".format(character))
	else:
		file.write("{0}, stages/{1}\n".format(character,stage))

def addStages(stage):
	file.write("stages/{0}\n".format(stage))

def addMusicToStage(stage):
	f = open("{0}.def".format(stage),"r+")
	f.close()




#get chars and stages
charList = getChars()
stageName - getStages()

#write the list of characters to a text file
def writeToFile():
	spaces = '->\n'
	breakLine = ';---------------------------------------------------------------------\n\n\n'

	#change to select def directory
	os.chdir(selectDir)

	file = open(select, "w")
	file.write(breakLine)
	file.write('[Characters]\n')
	file.write('randomselect\n')
	for item in charList: #place in addChar
		if item == 'MVC2_DrDoom':
			file.write("%s, stages/drdoombg.def\n" %item)
		else:
			file.write("%s\n" %item)

	#write the list of stages
	file.write(breakLine)
	file.write('[ExtraStages]\n')
	for item in stageName:
		file.write("stages/%s\n" %item)

	#write the options
	file.write(breakLine)
	file.write('[Options]\n')
	file.write('arcade.maxmatches = 6,1,1,0,0,0,0,0,0,0\n')
	file.write('team.maxmatches = 4,1,1,0,0,0,0,0,0,0\n')	

	file.close()


