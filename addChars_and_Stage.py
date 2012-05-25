import os, glob
directory = os.getcwd()							#get the directory
select = 'select.def'							#select.def file


#Name Directories
charDir = directory + '\\chars'					#Folder for characters
stageDir = directory + '\\stages'				#Folder for stages
selectDir = directory + '\\data'				#Folder for select.def

print charDir
print stageDir
print selectDir

#get the list of characters
charList =  [f for f in os.listdir(charDir)
            if os.path.isdir(os.path.join(charDir, f))]
print charList

#get the list of stages
os.chdir(stageDir)							#change the directory to the stage directory
stageName = glob.glob('*.def')				#search for only the .def files
print stageName



#change to select def directory
os.chdir(selectDir)
spaces = '->\n'

#write the list of characters to a text file
file = open(select, "w")
file.write(';---------------------------------------------------------------------\n')
file.write('[Characters]\n')
file.write('randomselect\n')
for item in charList:
	if item == 'MVC2_DrDoom':
		file.write("%s, stages/drdoombg.def\n" %item)
	else:
		file.write("%s\n" %item)

#write the list of stages
file.write('\n\n;---------------------------------------------------------------------\n')
file.write('[ExtraStages]\n')
for item in stageName:
    file.write("stages/%s\n" %item)

#write the options
file.write('\n\n;---------------------------------------------------------------------\n')
file.write('[Options]\n')
file.write('arcade.maxmatches = 6,1,1,0,0,0,0,0,0,0\n')
file.write('team.maxmatches = 4,1,1,0,0,0,0,0,0,0\n')

file.close()


