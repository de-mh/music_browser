from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label, FileBrowser
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
from asciimatics.effects import Cog
import os

class mainView(Frame):
	def __init__(self, screen):
		super(mainView,self).__init__(screen,screen.height * 2 // 3,screen.width * 2 // 3,hover_focus=True,title="music finder")
		


		self.fileslist = os.listdir()
		self.dirlist = [("up..",0)]
		i = 1
		for l in self.fileslist:
				if os.path.isdir(l):
					self.dirlist.append((l,i))
					i+=1

		for l in self.fileslist:
			if l.endswith("mp3"):
				self.dirlist.append((l,i))
				i+=1


		layout = Layout([100], fill_frame=True)
		self.add_layout(layout)
		lable1 = Label(self.curdir.format(os.getcwd()))
		layout.add_widget(Divider())
		flbr = ListBox(10, self.dirlist,on_select=self._enter,name="flb")
		button1 = Button("quit",self._quit)
		button2 = Button("Enter",self._enter)
		layout.add_widget(lable1)
		layout.add_widget(flbr)
		layout.add_widget(Divider())
		layout2 = Layout([1,1])
		self.add_layout(layout2)
		layout2.add_widget(button1,1)
		layout2.add_widget(button2,0)
		self.fix()

	
	curdir = "current directory: {0}"
	fileslist = os.listdir()
	dirlist = [("up..",0)]
	

	def _quit(self):
   		sys.exit(0)
	def _enter(self):
		self.save()
		if self.dirlist[self.data["flb"]][0] == "up..":
			os.chdir("..")
			print(os.getcwd())
		if os.path.isdir(self.dirlist[self.data["flb"]][0]):
			os.chdir(self.dirlist[self.data["flb"]][0])
		if self.dirlist[self.data["flb"]][0].endswith("mp3"):
			os.system(self.dirlist[self.data["flb"]][0])
		raise StopApplication("User pressed quit")
	
 	#@staticmethod
    #def _quit():
    #    raise StopApplication("User pressed quit")




def demo(screen):
	screen.clear()
	frame1 = mainView(screen)
	scenes = [Scene([frame1], duration=-1, name="main")]
	screen.play(scenes)

while True:
	Screen.wrapper(demo)
