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

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self,parent,title=title, size=(640,480))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.CreateStatusBar()

		#Setting up the menu
		filemenu = wx.Menu()

		filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
		filemenu.AppendSeperator()
		filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")

		#Creating the menubar
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)




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

#change to select def directory
os.chdir(selectDir)
spaces = '->\n'
breakLine = ';---------------------------------------------------------------------\n\n\n'

#get chars and stages
charList = getChars()
stageName - getStages()

#write the list of characters to a text file
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

#Run the app
app = wx.App(False)
frame = MainWindow(None, "M.U.G.E.N Add Characters and Stages")
app.MainLoop()

